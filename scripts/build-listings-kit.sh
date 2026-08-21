#!/usr/bin/env bash
# Build a dated, ready-to-upload local-listings asset folder from Cloudinary.
# Per-platform crops are generated server-side — no manual resizing.
# Usage: bash scripts/build-listings-kit.sh [outdir]
set -euo pipefail

CLOUD="drxrfyq9i"
GRADE="e_saturation:18,e_contrast:10,e_brightness:4"
STAMP="$(date +%Y%m%d)"
HQ="$HOME/Documents/Uno-mas-hq-2026/listings"
OUT="${1:-$HQ/uno-mas-listings-kit-$STAMP}"
mkdir -p "$(dirname "$OUT")"

HERO=(
  20251217_UM_VENUE_VenueInterior_FINAL_11
  20251217_UM_VENUE_VenueInterior_FINAL_01
  20251217_UM_VENUE_VenueInterior_FINAL_12
  20260125_UM_VENUE_InteriorDownstairsBar_FINAL
  20260623_UM_VENUE_PapelPicadoDiningRoom01
  20260623_UM_VENUE_TealDiningRoomTables
  20260623_UM_VENUE_GameDayBarLounge
  20260623_UM_VENUE_NeonTubeGlasses
)
PATIO=( 20260623_UM_PATIO_PatioStringLights 20260623_UM_PATIO_PatioUmbrellaTable patio-daytime-blue-umbrellas )
FOOD=(
  20260125_UM_FOOD_TacoCloseUpV10_FINAL 20260125_UM_FOOD_FoodOnTable_FINAL
  20260623_UM_FOOD_SkirtSteakFlameGrill 20260623_UM_FOOD_LoadedCarneNachos
  20260623_UM_FOOD_MexicanHotDogPlated carne-asada-knife-hero
  20260204_UM_FOOD_FiestaPack_FINAL 20260207_UM_DRINK_PitcherAndMarg_FINAL
)
MEZZ=(
  20251028_MEZZ_VENUE_MezzSeatingAndBar_RAW 20251028_MEZZ_VENUE_MezzFireplace_RAW
  20251028_MEZZ_VENUE_MezzLounge_RAW 20251028_MEZZ_VENUE_MezzMural_RAW
  20251028_MEZZ_VENUE_MezzBar_v1
)
VIDEO=( "ariel_view_-_drone_footage_of_uno_mas_2" brunch_food_paning_v3 20260623_UM_FOOD_GrilledSteakPlatter 20260623_UM_FOOD_UnoMasBurritoTable )

# name|transform  (crops per platform)
PROFILES=(
  "google-cover-1024x576|c_fill,g_auto,w_1024,h_576"
  "google-additional-1200x900|c_fill,g_auto,w_1200,h_900"
  "apple-hero-1920x1080|c_fill,g_auto,w_1920,h_1080"
  "yelp-wide-2000|c_limit,w_2000"
  "social-4x5-1080x1350|c_fill,g_auto,w_1080,h_1350"
  "social-9x16-1080x1920|c_fill,g_auto,w_1080,h_1920"
  "square-1080|c_fill,g_auto,w_1080,h_1080"
)

fetch () { # $1=public_id $2=transform $3=destfile
  local url="https://res.cloudinary.com/$CLOUD/image/upload/$2,$GRADE/q_auto,f_jpg/$1"
  if curl -fsSL "$url" -o "$3"; then
    printf '    ok  %s (%s)\n' "$(basename "$3")" "$(du -h "$3" | cut -f1)"
  else
    printf '    FAIL %s\n' "$1" >&2; return 0
  fi
}

echo "Uno Más listings kit → $OUT"
for prof in "${PROFILES[@]}"; do
  name="${prof%%|*}"; xf="${prof##*|}"
  echo "  [$name]"
  for grp in HERO PATIO FOOD; do
    eval "arr=( \"\${${grp}[@]}\" )"
    d="$OUT/$name/$(echo "$grp" | tr 'A-Z' 'a-z')"; mkdir -p "$d"
    for id in "${arr[@]}"; do fetch "$id" "$xf" "$d/${id}.jpg"; done
  done
done

echo "  [mezzanine — separate sub-brand, do NOT mix with Uno Más]"
d="$OUT/mezzanine"; mkdir -p "$d"
for id in "${MEZZ[@]}"; do fetch "$id" "c_fill,g_auto,w_1920,h_1080" "$d/${id}.jpg"; done

echo "  [video]"
d="$OUT/video"; mkdir -p "$d"
for id in "${VIDEO[@]}"; do
  url="https://res.cloudinary.com/$CLOUD/video/upload/c_fill,g_center,w_1920,h_1080,q_auto/$id.mp4"
  curl -fsSL "$url" -o "$d/${id}.mp4" \
    && printf '    ok  %s (%s)\n' "$id.mp4" "$(du -h "$d/${id}.mp4" | cut -f1)" \
    || printf '    FAIL %s\n' "$id" >&2
done

cp "$(dirname "${BASH_SOURCE[0]}")/../marketing/local-listings-asset-kit.md" "$OUT/README-copy-paste-text.md"

cat > "$OUT/UPLOAD-CHECKLIST.txt" <<'EOF'
UNO MÁS — LISTINGS UPLOAD CHECKLIST

[ ] Google Business Profile  → google-cover + google-additional + video
      Also: hours, description, attributes (Family-friendly ALL HOURS), menu link,
      weekly-specials Post
[ ] Apple Business Connect   → apple-hero + square-1080
[ ] Yelp                     → yelp-wide
[ ] Facebook / Instagram     → square-1080, social-4x5, social-9x16
[ ] TripAdvisor              → RENAME from "Uno Mas Taco Shop" → "Uno Más Tacos & Tequila", then yelp-wide
[ ] Resy                     → apple-hero set
[ ] Bing Places              → google-cover set

Text, hours, description and attributes: see README-copy-paste-text.md
Mezzanine assets are a SEPARATE sub-brand — never mix with Uno Más listings.
EOF

echo
echo "Done → $OUT"
echo "  $(find "$OUT" -type f | wc -l | tr -d ' ') files"
