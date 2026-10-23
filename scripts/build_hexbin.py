"""
Builds data/processed/aedc_lga_hexbins_px.csv for specs/17_lga_vulnerability_hexbin.vl.json.

Why this exists: Vega-Lite has no built-in hexbin, and when we tried the
obvious approach (a GeoJSON/TopoJSON layer of hexagon polygons, drawn with
a normal geoshape mark), every single hexagon came out as one shared,
canvas-filling blob instead of 125 small hexagons. Spent a while trying to
figure out if it was our geometry, but it turned out to be a real bug in
how Vega-Lite's auto-fit handles lots of small separate polygons - it
still happened with just one hexagon on the page by itself, and with both
GeoJSON and TopoJSON.

So instead we just do the projection math ourselves. Each LGA's lon/lat
gets projected to pixel coordinates in Python (same Albers projection, same
settings as every other map on the page), and the hex-binning happens in
that pixel space rather than in lon/lat - which also just looks better,
since Albers doesn't scale evenly and binning in lon/lat would give you
squashed hexagons. The output is just 6 corner points per hexagon (plus one
repeated point to close the shape), and the chart draws them with a plain
line mark instead of geoshape.

Run from the repo root: python3 scripts/build_hexbin.py
"""
import csv
import math
from collections import defaultdict

# --- Albers equal-area conic projection (matches d3-geo's albers()) ---

def make_albers_projector(rotate_lambda, parallel1, parallel2, center_lat):
    phi1 = math.radians(parallel1)
    phi2 = math.radians(parallel2)
    phi0 = math.radians(center_lat)
    lambda0 = math.radians(-rotate_lambda)  # d3's rotate is the negative of the central meridian

    n = (math.sin(phi1) + math.sin(phi2)) / 2
    C = math.cos(phi1) ** 2 + 2 * n * math.sin(phi1)
    rho0 = math.sqrt(C - 2 * n * math.sin(phi0)) / n

    def project(lon, lat):
        phi = math.radians(lat)
        lam = math.radians(lon) - lambda0
        rho = math.sqrt(C - 2 * n * math.sin(phi)) / n
        theta = n * lam
        x = rho * math.sin(theta)
        y = rho0 - rho * math.cos(theta)
        return x, y

    return project


# Same rotate/parallels/center as the other maps in this project (specs/03,
# 04, 13, 16), so this lines up with them.
PROJ = make_albers_projector(rotate_lambda=-132, parallel1=-18, parallel2=-36, center_lat=-27)

# These are just the scale/translate values Vega-Lite's own auto-fit picked
# when we rendered the state outline alone at our usual 760x664 map size -
# we read them straight off that render and reused them here, since the two
# layers need to agree on where things sit. Checked these against a few
# real cities (Sydney, Perth, Darwin, Melbourne, Hobart) to make sure they
# actually land in the right spot before trusting them.
SCALE = 1145.74
TRANSLATE = (358.94, 319.53)


def to_pixel(lon, lat):
    x, y = PROJ(lon, lat)
    # flip y: lat increases going north, but screen pixels increase going down
    return x * SCALE + TRANSLATE[0], -y * SCALE + TRANSLATE[1]


# --- Axial hex-grid binning in pixel space ---

def pixel_to_axial(x, y, size):
    q = (math.sqrt(3) / 3 * x - 1 / 3 * y) / size
    r = (2 / 3 * y) / size
    return axial_round(q, r)


def axial_round(q, r):
    x, z = q, r
    y = -x - z
    rx, ry, rz = round(x), round(y), round(z)
    x_diff, y_diff, z_diff = abs(rx - x), abs(ry - y), abs(rz - z)
    if x_diff > y_diff and x_diff > z_diff:
        rx = -ry - rz
    elif y_diff > z_diff:
        ry = -rx - rz
    else:
        rz = -rx - ry
    return int(rx), int(rz)


def axial_to_pixel(q, r, size):
    x = size * math.sqrt(3) * (q + r / 2)
    y = size * 1.5 * r
    return x, y


def hex_corners_px(cx, cy, size):
    corners = []
    for i in range(6):
        angle = math.pi / 180 * (60 * i - 30)  # pointy-top orientation
        corners.append((cx + size * math.cos(angle), cy + size * math.sin(angle)))
    return corners


HEX_RADIUS_PX = 20  # just tuned by eye to get a reasonable hex size on the 760x664 canvas


def main():
    rows = list(csv.DictReader(open('data/processed/aedc_lga_2024_with_centroids.csv')))
    points = []
    for r in rows:
        if not r['vulnerable_1plus_pct']:
            continue
        points.append({
            'lat': float(r['lat']),
            'lon': float(r['lon']),
            'pct': float(r['vulnerable_1plus_pct']),
            'n': float(r['vulnerable_1plus_valid_n']) if r['vulnerable_1plus_valid_n'] else 0,
        })
    print(f'{len(points)} points with valid data')

    bins = defaultdict(list)
    for p in points:
        px, py = to_pixel(p['lon'], p['lat'])
        q, r = pixel_to_axial(px, py, HEX_RADIUS_PX)
        bins[(q, r)].append(p)
    print(f'{len(bins)} occupied hex bins')

    # Also draw empty hexagons, but only right next to a real one - otherwise
    # we'd end up drawing hexagons out over open ocean again, which is the
    # whole reason the outline got dropped in the first place. A gap that's
    # actually inside the pattern (next to real data) is worth showing as an
    # outlined-but-empty cell, so it reads as "no data here" rather than
    # looking like a random missing puzzle piece.
    AXIAL_NEIGHBOURS = [(1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1), (0, 1)]
    empty_bins = set()
    for (q, r) in bins:
        for dq, dr in AXIAL_NEIGHBOURS:
            neighbour = (q + dq, r + dr)
            if neighbour not in bins:
                empty_bins.add(neighbour)
    print(f'{len(empty_bins)} empty neighbouring bins (drawn outlined, no fill)')

    out_rows = []

    def add_hex(q, r, bin_id, has_data, avg_pct=None, n_lgas=0, total_children=0):
        cx, cy = axial_to_pixel(q, r, HEX_RADIUS_PX * 0.95)  # shrink slightly so hexes don't touch
        corners = hex_corners_px(cx, cy, HEX_RADIUS_PX * 0.95)
        for i, (cx_, cy_) in enumerate(corners):
            out_rows.append({
                'bin_id': bin_id, 'order': i, 'x': round(cx_, 2), 'y': round(cy_, 2),
                'has_data': 'true' if has_data else 'false',  # lowercase: Vega's boolean parser wants this, not Python's True/False
                'avg_pct': round(avg_pct, 2) if avg_pct is not None else '',
                'n_lgas': n_lgas, 'total_children': total_children,
            })
        # repeat the first corner at the end so the line mark closes the hexagon properly
        first = dict(out_rows[-6])
        first['order'] = 6
        out_rows.append(first)

    for (q, r), pts in bins.items():
        total_n = sum(p['n'] for p in pts)
        weighted_pct = (
            sum(p['pct'] * p['n'] for p in pts) / total_n
            if total_n > 0
            else sum(p['pct'] for p in pts) / len(pts)
        )
        add_hex(q, r, f'{q}_{r}', has_data=True, avg_pct=weighted_pct, n_lgas=len(pts), total_children=int(total_n))

    for (q, r) in empty_bins:
        add_hex(q, r, f'{q}_{r}', has_data=False)

    print(f'{len(out_rows)} vertex rows '
          f'({len(bins)} filled + {len(empty_bins)} empty hexagons x 7, incl. closing vertex)')

    with open('data/processed/aedc_lga_hexbins_px.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['bin_id', 'order', 'x', 'y', 'has_data', 'avg_pct', 'n_lgas', 'total_children'])
        w.writeheader()
        w.writerows(out_rows)
    print('wrote data/processed/aedc_lga_hexbins_px.csv')


if __name__ == '__main__':
    main()
