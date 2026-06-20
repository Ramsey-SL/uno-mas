# Uno Más — DAM Workflow (Cloudinary)

How assets get into the **DAM (Cloudinary cloud `drxrfyq9i`)** and organized in Google Drive.
Part of the 3-tier model: GitHub = brain · **Cloudinary = DAM** · Drive = warehouse. See `CLAUDE.md`.

## The convention
**Mark any asset for the DAM by putting `website` in its filename.** Then it gets uploaded to
Cloudinary and sorted into the Drive library. (Originated as "website assets," now the general
"approve for DAM" marker.)

## Scripts (live on Drive, not in this repo — they're code)
`Ramsey-HQ/Plugins-and-Apps/dam-tools/`:
- **`dam-sort.sh`** — manifest (`path|category|DescriptiveName`) → upload to Cloudinary (descriptive
  public_id + display_name + tags) + rename & move the local file into its Drive category folder. Images & video.
- **`cloudinary-upload.sh`** — generic signed uploader (env creds).
- **`extract-frames.sh`** — one frame per video (needs ffmpeg) for visual categorization.
- `README.md` — full usage + the category→Drive-folder map.

## The pipeline
1. `export CLOUDINARY_API_KEY/SECRET` (key needs Upload + Admin permissions).
2. `find <folder> -type f | grep -i website` → asset list.
3. **Categorize** (the AI step, done with Claude): view each image / video frame, assign category +
   descriptive name → build a manifest. For already-foldered assets, category can be derived from the
   folder path instead (no vision needed).
4. `dam-sort.sh manifest.txt YYYYMMDD` → uploads, renames, sorts. Names match in Drive **and** DAM.

## Cloudinary structure & tags
- Photos → `uno-mas/photos/<category>` · videos → `uno-mas/videos/<category>` or `uno-mas/website/video`
  · channel-ready library → `uno-mas/website/<category>`.
- Tag taxonomy (see `brand-context-pack.md`): `category:*`, `role:*` (hero-cantina, hero-dinner…),
  venue/brand (cantina, patio, mezzanine, uno-mas), plus batch tags (`import-<date>`, `channel-ready`, `website`).
- Categories: food, cantina-interior, cocktails, patio, mezzanine, team-people, event, menu, signage-decor, general-vibe.

## ⚠️ Free-plan limits
~25 monthly credits, images ≤10 MB, **videos ≤100 MB**. Oversized videos must be compressed first.
Cloudinary holds the **curated/approved** set — the Drive `Uno Mas Marketing HQ` library stays the master.

## History
- 2026-06-19: built the pipeline; processed Unsorted Asseets (138 images + 52 videos, vision-categorized,
  renamed, sorted DAM + Drive); bulk-uploaded the `_CHANNEL_READY/Website` approved set (deduped). See
  `[[project_cloudinary_dam]]` memory for the live resume point.
