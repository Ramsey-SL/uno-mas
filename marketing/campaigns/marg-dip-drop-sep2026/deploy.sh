#!/bin/bash
# Rebuild and redeploy the promo page to https://unomas-promo-drop.netlify.app
set -e
cd "$(dirname "$0")"
python3 gen.py
rm -rf _site && mkdir -p _site
cp promo-overview.html _site/index.html
cp style.css _site/style.css
cat > _site/netlify.toml <<'TOML'
[build]
  publish = "."
[[headers]]
  for = "/*"
  [headers.values]
    X-Robots-Tag = "noindex, nofollow, noarchive, nosnippet"
    Cache-Control = "no-store"
TOML
printf 'User-agent: *\nDisallow: /\n' > _site/robots.txt
echo "built _site/ — now run the netlify deploy command for site 4c5fc602-5eff-49af-b555-a5588a9ee905"
echo "  (ask Claude to re-issue it; the proxy token is short-lived)"
