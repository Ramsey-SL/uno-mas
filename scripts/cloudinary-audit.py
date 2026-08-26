#!/usr/bin/env python3
"""
Uno Más — Cloudinary DAM audit.

Runs the full inventory the moment credentials exist. Read-only: it never
uploads, renames, retags or deletes. Every finding is reported, not fixed.

    export CLOUDINARY_URL='cloudinary://<api_key>:<api_secret>@drxrfyq9i'
    python3 scripts/cloudinary-audit.py            # summary
    python3 scripts/cloudinary-audit.py --csv out.csv

Needs a Master/full-access key. A restricted key returns
`missing permissions actions=[create]` on some endpoints; search is read-only
so a read-scoped key is fine for this script.
"""
import base64, csv, json, os, re, sys, urllib.parse, urllib.request

CLOUD = "drxrfyq9i"
# Assets store their folder EITHER in asset_folder (dynamic folders) OR as a
# path inside public_id (the older website/buildout set). Matching only one
# field silently misses part of the library — this is the documented gotcha.
SCOPE = ("(asset_folder:uno-mas/* OR public_id:uno-mas/* OR "
         "asset_folder:mezzanine/* OR public_id:mezzanine/*)")

# The shared-album derivatives are EXACTLY 2048 on the long edge. A naive
# `long_edge < 2000` test passes them as print-ok, which is the precise
# failure this gate exists to prevent. Anything at or under 2048 is suspect.
SHARED_ALBUM_LONG_EDGE = 2048
PRINT_MIN_LONG_EDGE = 2400

NAME_RE = re.compile(r"^\d{8}_UM_[A-Z]+_[A-Za-z0-9]+(_[A-Za-z0-9#]+)?$")


def auth_header():
    url = os.environ.get("CLOUDINARY_URL", "")
    m = re.match(r"cloudinary://([^:]+):([^@]+)@(.+)", url)
    if not m:
        sys.exit("Set CLOUDINARY_URL='cloudinary://<key>:<secret>@drxrfyq9i' first.")
    key, secret, cloud = m.groups()
    if cloud != CLOUD:
        print(f"  ! CLOUDINARY_URL points at '{cloud}', expected '{CLOUD}'", file=sys.stderr)
    tok = base64.b64encode(f"{key}:{secret}".encode()).decode()
    return {"Authorization": f"Basic {tok}", "Content-Type": "application/json"}, cloud


def api(path, cloud, hdrs, payload=None, method="GET"):
    url = f"https://api.cloudinary.com/v1_1/{cloud}/{path}"
    data = json.dumps(payload).encode() if payload else None
    req = urllib.request.Request(url, data=data, headers=hdrs, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code} on {path}: {e.read().decode()[:400]}")


def fetch_all(cloud, hdrs):
    out, cursor = [], None
    while True:
        body = {"expression": SCOPE, "max_results": 500,
                "with_field": ["tags", "context"],
                "sort_by": [{"public_id": "asc"}]}
        if cursor:
            body["next_cursor"] = cursor
        res = api("resources/search", cloud, hdrs, body, "POST")
        out.extend(res.get("resources", []))
        cursor = res.get("next_cursor")
        print(f"  … {len(out)} assets", file=sys.stderr)
        if not cursor:
            return out, res.get("total_count", len(out))


def main():
    hdrs, cloud = auth_header()
    print("Usage / plan:")
    usage = api("usage", cloud, hdrs)
    for k in ("plan", "credits", "storage", "bandwidth", "transformations", "resources"):
        if k in usage:
            print(f"  {k}: {json.dumps(usage[k])[:160]}")

    print("\nEnumerating library…", file=sys.stderr)
    assets, total = fetch_all(cloud, hdrs)
    print(f"\n=== {len(assets)} assets returned (search total_count: {total}) ===")

    folders, tags, findings = {}, {}, []
    for a in assets:
        pid = a.get("public_id", "")
        folder = a.get("asset_folder") or ("/".join(pid.split("/")[:-1]) or "<Home>")
        folders[folder] = folders.get(folder, 0) + 1
        atags = a.get("tags") or []
        for t in atags:
            tags[t] = tags.get(t, 0) + 1

        w, h = a.get("width") or 0, a.get("height") or 0
        long_edge = max(w, h)
        base = pid.split("/")[-1]

        if a.get("resource_type") == "image" and long_edge:
            suspect = long_edge <= SHARED_ALBUM_LONG_EDGE
            tagged = "needs-hires-swap" in atags
            if suspect and not tagged:
                findings.append(("UNTAGGED-LOWRES", pid, f"{w}x{h} — low-res but NOT tagged needs-hires-swap"))
            if not suspect and tagged and long_edge >= PRINT_MIN_LONG_EDGE:
                findings.append(("OVERTAGGED", pid, f"{w}x{h} — tagged needs-hires-swap but is print-capable"))
        if not NAME_RE.match(base):
            findings.append(("NAMING", pid, f"'{base}' does not match YYYYMMDD_UM_<CAT>_<Subject>[_v#]"))
        if "hero-approved" in atags:
            findings.append(("HERO", pid, f"{w}x{h}"))

    print("\n--- Folders ---")
    for f, n in sorted(folders.items(), key=lambda x: -x[1]):
        print(f"  {n:>5}  {f}")
    print("\n--- Tags ---")
    for t, n in sorted(tags.items(), key=lambda x: -x[1]):
        print(f"  {n:>5}  {t}")

    print("\n--- Findings ---")
    by_kind = {}
    for kind, pid, note in findings:
        by_kind.setdefault(kind, []).append((pid, note))
    for kind in ("UNTAGGED-LOWRES", "OVERTAGGED", "NAMING", "HERO"):
        rows = by_kind.get(kind, [])
        print(f"\n  [{kind}] {len(rows)}")
        for pid, note in rows[:40]:
            print(f"     {pid}  —  {note}")
        if len(rows) > 40:
            print(f"     … and {len(rows)-40} more")

    if not by_kind.get("HERO"):
        print("\n  ** No asset carries `hero-approved`. That tag does not exist yet. **")

    if "--csv" in sys.argv:
        path = sys.argv[sys.argv.index("--csv") + 1]
        with open(path, "w", newline="") as fh:
            wtr = csv.writer(fh)
            wtr.writerow(["public_id", "folder", "w", "h", "long_edge", "bytes", "format", "tags"])
            for a in assets:
                pid = a.get("public_id", "")
                wtr.writerow([pid,
                              a.get("asset_folder") or "/".join(pid.split("/")[:-1]),
                              a.get("width"), a.get("height"),
                              max(a.get("width") or 0, a.get("height") or 0),
                              a.get("bytes"), a.get("format"),
                              "|".join(a.get("tags") or [])])
        print(f"\nWrote {path}")


if __name__ == "__main__":
    main()
