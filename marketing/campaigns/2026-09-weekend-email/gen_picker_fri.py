from _shared import *
CROP = "f_auto,q_auto:best,w_1200,h_800,c_fill,g_auto,e_vibrance:22"
F="uno-mas/photos/food"; A="uno-mas/approved-assets/photos"

OPTS=[
 (f"{F}/20260619_UM_FOOD_TwoTacosMetalTray","Two Tacos, Metal Tray","2242×1536 native landscape","Two street tacos on a branded metal tray. This is <em>literally</em> the offer — two tacos, $10 — and it's the widest native landscape in the set, so it crops with room to spare.","Best match"),
 (f"{F}/20260619_UM_FOOD_TacosJarritosGrapefruit","Tacos + Jarritos","2112×1536 native landscape","Tacos with a drink in frame. Reads as the full late-night order rather than just food, which suits a happy hour better than a bare plate.","Food + drink"),
 (f"{F}/20260619_UM_FOOD_TacosRadishCarnitas","Carnitas Tacos, Radish","2048×2048 square","Tight, colorful carnitas tacos. Square source means a gentle crop either direction.",""),
 (f"{F}/20260619_UM_FOOD_TortillaCharringFlames","Tortilla Charring, Flames","1536×2048 portrait","Tortillas charring over open flame. Dark and moody — the only shot here that <em>feels</em> like 10pm rather than lunch. Crops tight, but the flame carries it.","Moodiest"),
 ("20260623_UM_VENUE_TacosNeonHallway","Tacos Neon Hallway","2048×1536 native landscape","The neon TACOS sign. No food at all — sells the room and the hour. Pairs well if you'd rather the copy do the selling.","Atmosphere"),
]
MEZZ=("20251028_MEZZ_VENUE_MezzBar_v1","Mezzanine Bar","2730×1536 native landscape","Genuinely the best late-night <em>looking</em> image in the DAM — dark, moody, bar-forward.")

items=""
for i,(pid,name,dims,desc,tag) in enumerate(OPTS,1):
    tagh=f'<span class="tag">{tag}</span>' if tag else ''
    items+=f"""<div class="opt"><img src="{B}/{CROP}/{pid}" alt="{name}" loading="lazy">
      <div class="ob"><div class="oh"><span class="num">FRI-{chr(64+i)}</span><strong>{name}</strong>{tagh}</div>
      <p class="dims">{dims}</p><p class="desc">{desc}</p><code>{pid}</code></div></div>"""

pid,name,dims,desc = MEZZ
mezz=f"""<div class="opt warn"><img src="{B}/{CROP}/{pid}" alt="{name}" loading="lazy">
  <div class="ob"><div class="oh"><span class="num" style="background:#FFEC00">FRI-F</span><strong>{name}</strong><span class="tag" style="background:#4a2a00;color:#ffb84d">Brand caution</span></div>
  <p class="dims">{dims}</p><p class="desc">{desc}</p>
  <p class="desc" style="color:#ffb84d"><strong>But:</strong> this is The Mezzanine, a separate sub-brand with its own palette and type. The brand rules say never mix Uno Más and Mezzanine elements in one design, and Late Night Happy Hour runs downstairs in the Cantina. Using it would put Mezzanine imagery under an Uno Más header and imply the promo is upstairs. I'd avoid it — but it's your brand, so it's here.</p>
  <code>{pid}</code></div></div>"""

html=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Friday tile — new image options</title>
<link href="https://fonts.googleapis.com/css2?family=Antonio:wght@600;700&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
body{{margin:0;background:#111418;color:#e8ecf1;font-family:Montserrat,system-ui,sans-serif}}
header{{padding:26px 30px 20px;border-bottom:1px solid #232830}}
h1{{margin:0 0 6px;font-family:Antonio,sans-serif;font-size:30px;text-transform:uppercase}}
.sub{{margin:0;font-size:13px;color:#8d97a5;max-width:800px;line-height:20px}}
.locked{{margin:16px 30px 0;padding:12px 16px;background:#16241a;border-left:4px solid #3ddc84;border-radius:0 6px 6px 0;font-size:13px;color:#a8d8bb;line-height:20px}}
.row{{display:flex;gap:18px;overflow-x:auto;padding:24px 30px 30px}}
.opt{{flex:0 0 auto;width:340px;background:#1a1e25;border:1px solid #2a303a;border-radius:10px;overflow:hidden}}
.opt.warn{{border-color:#4a3a1a}}
.opt img{{width:340px;height:227px;object-fit:cover;display:block;background:#0d1014}}
.ob{{padding:13px 14px 15px}}
.oh{{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:5px}}
.num{{font:700 10px Montserrat,sans-serif;letter-spacing:.08em;color:#0d1014;background:#18BCDC;padding:3px 7px;border-radius:3px}}
.oh strong{{font-size:14px;color:#fff}}
.tag{{font:700 9.5px Montserrat,sans-serif;letter-spacing:.1em;text-transform:uppercase;padding:3px 7px;border-radius:3px;background:#0f2a30;color:#18BCDC}}
.dims{{margin:0 0 8px;font-size:11px;color:#5f6b7a;letter-spacing:.03em}}
.desc{{margin:0 0 9px;font-size:12.5px;line-height:19px;color:#96a0ae}}
code{{font-size:10.5px;color:#5f6b7a;word-break:break-all;display:block}}
</style></head><body>
<header><h1>Friday tile — new options</h1>
<p class="sub">All new — none of these were in the first round. Cropped exactly as the email crops (<code style="display:inline;color:#7fb2e8">w_1200 h_800 c_fill g_auto</code>).</p></header>
<div class="locked"><strong>Locked in:</strong> SAT-1 Chips &amp; Guac Trio v1 · SUN-2 Churro French Toast v4. Both already applied to the hybrid build.</div>
<div class="row">{items}{mezz}</div>
</body></html>"""
open("image-options-friday.html","w").write(html)
open("_urls_fri.txt","w").write("\n".join(f"{B}/{CROP}/{p}" for p,_,_,_,_ in OPTS)+f"\n{B}/{CROP}/{MEZZ[0]}\n")
print("wrote friday picker")
