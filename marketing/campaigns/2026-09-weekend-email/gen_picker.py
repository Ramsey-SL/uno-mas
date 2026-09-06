from _shared import *
import json, subprocess

CROP = "f_auto,q_auto:best,w_1200,h_800,c_fill,g_auto,e_vibrance:22"
P="uno-mas/approved-assets/photos"

TILES = [
 ("fri","Friday — Late Night Happy Hour","#18BCDC","Needs to say <em>two street tacos, $10</em> at a glance, or read as late-night atmosphere.",[
   (f"{P}/food/20260724_UM_FOOD_StreetTaco_v3","Street Taco v3","Native landscape, shot Jul 2026. Cleanest single-taco hero — crops without losing the subject.","Recommended"),
   ("20260623_UM_FOOD_TwoStreetTacosTray","Two Street Tacos Tray","Literally two tacos, which matches the offer exactly. Currently used in mockups 1–5.","Most literal"),
   (f"{P}/food/20260724_UM_FOOD_StreetTaco_v2","Street Taco v2","Same session, different angle. Landscape.",""),
   ("20260623_UM_VENUE_TacosNeonDiningRoom","Tacos Neon Dining Room","Room shot with neon — sells the late-night mood rather than the food.","Atmosphere"),
   ("20260623_UM_VENUE_UnoMasNeonBarSign","Uno Más Neon Bar Sign","Bar neon. Darkest option, closest to the dark slide treatment.","Atmosphere"),
 ]),
 ("sat","Saturday — $25 Margs + Chips &amp; Dip","#E22690","The current photo is <strong>loaded carne nachos</strong>, which is not chips and dip. These actually match the offer.",[
   (f"{P}/food/20260814_UM_FOOD_ChipsGuacTrio_v1","Chips &amp; Guac Trio v1","Native landscape, Aug 2026. Chips with a trio of dips — the closest thing in the DAM to the actual offer.","Recommended"),
   (f"{P}/food/20260814_UM_FOOD_ChipsGuacTrio_v6","Chips &amp; Guac Trio v6","Same session, alternate frame. Landscape.",""),
   (f"{P}/food/20260730_UM_FOOD_ChipsSalsa_v2","Chips &amp; Salsa v2","Simpler — chips and salsa only. Landscape.",""),
   (f"{P}/cocktails/20260724_UM_COCKTAILS_HouseMargarita_v2","House Margarita v2","The actual house marg being sold. Leads on the drink instead of the food.","Drink-led"),
   (f"{P}/cocktails/20260723_UM_COCKTAILS_MargaritaFlight_v3","Margarita Flight v3","Multiple margs in frame — reads as “two margs” better than a single glass. Landscape.","Drink-led"),
 ]),
 ("sun","Sunday — Brunch","#C79A16","Should look like a reason to book a table on a Sunday morning.",[
   (f"{P}/brunch/20260724_UM_BRUNCH_FrenchToastPrep_v3","French Toast Prep v3","Native landscape — the only brunch shot that doesn't need a hard vertical crop.","Recommended"),
   (f"{P}/brunch/20260724_UM_BRUNCH_ChurroFrenchToast_v4","Churro French Toast v4","The hero dish. Used in mockups 1–5. Portrait, so it crops tighter.","Current"),
   (f"{P}/brunch/20260724_UM_BRUNCH_ChurroFrenchToast_v2","Churro French Toast v2","Alternate frame, same dish.",""),
   (f"{P}/brunch/20260724_UM_BRUNCH_ChurroFrenchToast_v6","Churro French Toast v6","Alternate frame, same dish.",""),
   (f"{P}/venue/20260724_UM_VENUE_GuestsToasting_v4","Guests Toasting v4","People, not plates. Sells the occasion — arguably the better reservations driver.","People"),
 ]),
]

cards=""
for key,title,color,note,opts in TILES:
    items=""
    for i,(pid,name,desc,tag) in enumerate(opts,1):
        tagh=f'<span class="tag" style="background:{color}22;color:{color}">{tag}</span>' if tag else ''
        items+=f"""
      <div class="opt">
        <img src="{B}/{CROP}/{pid}" alt="{name}" loading="lazy">
        <div class="ob">
          <div class="oh"><span class="num" style="background:{color}">{key.upper()}-{i}</span><strong>{name}</strong>{tagh}</div>
          <p class="desc">{desc}</p>
          <code>{pid}</code>
        </div>
      </div>"""
    cards+=f"""
  <section>
    <h2 style="border-left:6px solid {color}">{title}</h2>
    <p class="note">{note}</p>
    <div class="row">{items}</div>
  </section>"""

html=f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Image options — Friday email</title>
<link href="https://fonts.googleapis.com/css2?family=Antonio:wght@600;700&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
body{{margin:0;background:#111418;color:#e8ecf1;font-family:Montserrat,system-ui,sans-serif}}
header{{padding:26px 30px 20px;border-bottom:1px solid #232830}}
h1{{margin:0 0 6px;font-family:Antonio,sans-serif;font-size:30px;text-transform:uppercase}}
.sub{{margin:0;font-size:13px;color:#8d97a5;max-width:760px;line-height:20px}}
section{{padding:26px 30px 8px}}
h2{{font-family:Antonio,sans-serif;font-size:23px;text-transform:uppercase;margin:0 0 8px;padding-left:12px}}
.note{{margin:0 0 16px;font-size:13px;color:#939dab;max-width:780px;line-height:20px}}
.row{{display:flex;gap:18px;overflow-x:auto;padding-bottom:14px}}
.opt{{flex:0 0 auto;width:330px;background:#1a1e25;border:1px solid #2a303a;border-radius:10px;overflow:hidden}}
.opt img{{width:330px;height:220px;object-fit:cover;display:block;background:#0d1014}}
.ob{{padding:13px 14px 15px}}
.oh{{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:7px}}
.num{{font:700 10px Montserrat,sans-serif;letter-spacing:.08em;color:#0d1014;padding:3px 7px;border-radius:3px}}
.oh strong{{font-size:14px;color:#fff}}
.tag{{font:700 9.5px Montserrat,sans-serif;letter-spacing:.1em;text-transform:uppercase;padding:3px 7px;border-radius:3px}}
.desc{{margin:0 0 9px;font-size:12.5px;line-height:19px;color:#96a0ae}}
code{{font-size:10.5px;color:#5f6b7a;word-break:break-all;display:block}}
footer{{padding:20px 30px 50px;font-size:12.5px;color:#8d97a5;line-height:20px}}
</style></head><body>
<header>
  <h1>Image options — Friday email</h1>
  <p class="sub">Every option below is cropped exactly as the email will crop it (<code style="display:inline;color:#7fb2e8">w_1200 h_800 c_fill g_auto</code>), so what you see is what sends. All from <code style="display:inline;color:#7fb2e8">uno-mas/approved-assets/</code>. Call out picks by code — e.g. &ldquo;FRI-2, SAT-4, SUN-1&rdquo;.</p>
</header>
{cards}
<footer>Current hybrid build uses <strong>FRI-1 · SAT-1 · SUN-1</strong>. Swap by editing <code style="display:inline">picks.json</code> and re-running <code style="display:inline">gen6.py</code>, or just tell me the codes.</footer>
</body></html>"""
open("image-options.html","w").write(html)
urls=[f"{B}/{CROP}/{p}" for _,_,_,_,o in TILES for p,_,_,_ in o]
open("_urls.txt","w").write("\n".join(urls))
print(f"wrote picker with {len(urls)} options")
