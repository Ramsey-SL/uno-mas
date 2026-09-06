from _shared import *
CROP="f_auto,q_auto:best,w_1200,h_800,c_fill,g_auto,e_vibrance:22"
F="uno-mas/photos/food"; A="uno-mas/approved-assets/photos/food"

OPTS=[
 ("20260623_UM_FOOD_StreetTacosWithMargarita01","Street Tacos + Margarita 01","1536×2048 portrait",
  "Street tacos <em>and</em> a margarita in one frame. This is the happy hour in a single photo — food and drink together, which is exactly what the $10 tacos + $6 margs offer is.","Best match"),
 ("20260623_UM_FOOD_StreetTacosWithMargarita02","Street Tacos + Margarita 02","1536×2048 portrait",
  "Same setup, second frame. Pick whichever composition you prefer.","Food + drink"),
 (f"{F}/20260619_UM_FOOD_TacosJarritosLime","Tacos + Jarritos, Lime","2048×2048 square",
  "Tacos with a Jarritos bottle. Square source so it crops evenly, and the drink gives it the full-order feel.","Food + drink"),
 ("20260623_UM_FOOD_StreetTacosPatioTable","Street Tacos, Patio Table","1536×2048 portrait",
  "Tacos on a full patio table — other plates and glassware in frame. Reads as a group sitting down, not a product shot.","Full table"),
 (f"{F}/20260619_UM_FOOD_TacosPatioUnoMasTray","Tacos, Branded Patio Tray","1536×2048 portrait",
  "Tacos on an Uno Más branded tray with the patio behind. Brand mark visible in the photo itself.","Full table"),
 ("20260623_UM_FOOD_StreetTacosPlate","Street Tacos, Plated","1536×2048 portrait",
  "Plated street tacos with pico. Cleaner and more composed than the table shots.",""),
 ("20260618_UM_FOOD_CarneTacos_v1","Carne Asada Tacos","1536×2048 portrait",
  "Carne asada with onion — and carne asada is one of the six meats actually on the $10 list, so it's literally on-menu.","On-menu meat"),
 ("20260623_UM_FOOD_GrillPlatterTacos","Grill Platter with Tacos","1536×2048 portrait",
  "Tacos as part of a bigger grill spread. The most food in frame of any option — reads generous.","Full table"),
 (f"{A}/20260723_UM_FOOD_BajaFishTaco_v4","Baja Fish Taco","2048×1536 native landscape",
  "The only wide native landscape here, so it crops with the most headroom. Note: Baja fish is <em>not</em> one of the six meats on the $10 late night list.","Crops best"),
]

items=""
for i,(pid,name,dims,desc,tag) in enumerate(OPTS,1):
    tagh=f'<span class="tag">{tag}</span>' if tag else ''
    items+=f"""<div class="opt"><img src="{B}/{CROP}/{pid}" alt="{name}" loading="lazy">
      <div class="ob"><div class="oh"><span class="num">FRI-{i}</span><strong>{name}</strong>{tagh}</div>
      <p class="dims">{dims}</p><p class="desc">{desc}</p><code>{pid}</code></div></div>"""

html=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Friday tile — taco scenes</title>
<link href="https://fonts.googleapis.com/css2?family=Antonio:wght@600;700&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
body{{margin:0;background:#111418;color:#e8ecf1;font-family:Montserrat,system-ui,sans-serif}}
header{{padding:26px 30px 20px;border-bottom:1px solid #232830}}
h1{{margin:0 0 6px;font-family:Antonio,sans-serif;font-size:30px;text-transform:uppercase}}
.sub{{margin:0;font-size:13px;color:#8d97a5;max-width:820px;line-height:20px}}
.locked{{margin:16px 30px 0;padding:12px 16px;background:#16241a;border-left:4px solid #3ddc84;border-radius:0 6px 6px 0;font-size:13px;color:#a8d8bb;line-height:20px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:18px;padding:24px 30px 40px}}
.opt{{background:#1a1e25;border:1px solid #2a303a;border-radius:10px;overflow:hidden}}
.opt img{{width:100%;height:225px;object-fit:cover;display:block;background:#0d1014}}
.ob{{padding:13px 14px 15px}}
.oh{{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:5px}}
.num{{font:700 10px Montserrat,sans-serif;letter-spacing:.08em;color:#0d1014;background:#18BCDC;padding:3px 7px;border-radius:3px}}
.oh strong{{font-size:14px;color:#fff}}
.tag{{font:700 9.5px Montserrat,sans-serif;letter-spacing:.1em;text-transform:uppercase;padding:3px 7px;border-radius:3px;background:#0f2a30;color:#18BCDC}}
.dims{{margin:0 0 8px;font-size:11px;color:#5f6b7a}}
.desc{{margin:0 0 9px;font-size:12.5px;line-height:19px;color:#96a0ae}}
code{{font-size:10.5px;color:#5f6b7a;word-break:break-all;display:block}}
</style></head><body>
<header><h1>Friday tile — taco scenes</h1>
<p class="sub">All contain tacos, most with drinks or a full table around them. Every one is new — none repeat from the two earlier rounds. Cropped exactly as the email crops (<code style="display:inline;color:#7fb2e8">w_1200 h_800 c_fill g_auto</code>).</p></header>
<div class="locked"><strong>Locked in:</strong> SAT-1 Chips &amp; Guac Trio v1 · SUN-2 Churro French Toast v4.</div>
<div class="grid">{items}</div>
</body></html>"""
open("image-options-friday.html","w").write(html)
open("_urls_fri.txt","w").write("\n".join(f"{B}/{CROP}/{p}" for p,_,_,_,_ in OPTS)+"\n")
print(f"wrote {len(OPTS)} options")
