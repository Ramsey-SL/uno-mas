from _shared import *
PID="20260207_UM_PROMO_StreetTacosInHolders_FINAL"
GRADE="e_auto_color,e_vibrance:40,e_saturation:18,e_contrast:16,e_sharpen:35"
VARIANTS=[
 ("A","Auto subject","g_auto",f"{GRADE}/f_auto,q_auto:best,w_1200,h_800,c_fill,g_auto","Cloudinary picks the subject. Default, and what the email is using now."),
 ("B","Centre","g_center",f"{GRADE}/f_auto,q_auto:best,w_1200,h_800,c_fill,g_center","Straight middle crop — predictable, ignores where the tacos actually sit."),
 ("C","Upper third","g_north",f"{GRADE}/f_auto,q_auto:best,w_1200,h_800,c_fill,g_north","Top of the frame."),
 ("D","Lower third","g_south",f"{GRADE}/f_auto,q_auto:best,w_1200,h_800,c_fill,g_south","Bottom of the frame."),
 ("E","Fit, no crop","c_pad",f"{GRADE}/f_auto,q_auto:best,w_1200,h_800,c_pad,b_auto","Whole photo, padded to fill. Nothing is cut, but you get bands either side."),
 ("F","Taller tile","4:3",f"{GRADE}/f_auto,q_auto:best,w_1200,h_900,c_fill,g_auto","Change the tile itself to 4:3 so the crop is less brutal. Affects all three tiles."),
]
UNGRADED=f"f_auto,q_auto:best,w_1200,h_800,c_fill,g_auto"
cards=""
for k,name,g,t,desc in VARIANTS:
    cards+=f"""<div class="opt"><img src="{B}/{t}/{PID}" alt="{name}" loading="lazy">
      <div class="ob"><div class="oh"><span class="num">{k}</span><strong>{name}</strong><span class="tag">{g}</span></div>
      <p class="desc">{desc}</p><code>{t}</code></div></div>"""
html=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Street Tacos in Holders — crop &amp; colour</title>
<link href="https://fonts.googleapis.com/css2?family=Antonio:wght@600;700&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
body{{margin:0;background:#111418;color:#e8ecf1;font-family:Montserrat,system-ui,sans-serif}}
header{{padding:26px 30px 20px;border-bottom:1px solid #232830}}
h1{{margin:0 0 6px;font-family:Antonio,sans-serif;font-size:28px;text-transform:uppercase}}
.sub{{margin:0;font-size:13px;color:#8d97a5;max-width:820px;line-height:20px}}
h2{{font-family:Antonio,sans-serif;font-size:20px;text-transform:uppercase;margin:26px 30px 4px}}
.note{{margin:0 30px 14px;font-size:12.5px;color:#8d97a5;max-width:820px;line-height:19px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:18px;padding:6px 30px 34px}}
.opt{{background:#1a1e25;border:1px solid #2a303a;border-radius:10px;overflow:hidden}}
.opt img{{width:100%;height:232px;object-fit:cover;display:block;background:#0d1014}}
.ob{{padding:13px 14px 15px}}
.oh{{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:6px}}
.num{{font:700 11px Montserrat,sans-serif;color:#0d1014;background:#FFEC00;padding:3px 8px;border-radius:3px}}
.oh strong{{font-size:14px;color:#fff}}
.tag{{font:600 10px Montserrat,sans-serif;padding:3px 7px;border-radius:3px;background:#0f2a30;color:#18BCDC}}
.desc{{margin:0 0 9px;font-size:12.5px;line-height:19px;color:#96a0ae}}
code{{font-size:10px;color:#5f6b7a;word-break:break-all;display:block}}
.pair{{display:grid;grid-template-columns:1fr 1fr;gap:18px;padding:6px 30px 30px}}
.pair figure{{margin:0}} .pair img{{width:100%;border-radius:8px;border:1px solid #2a303a;display:block}}
.pair figcaption{{font-size:12px;color:#8d97a5;padding-top:8px}}
</style></head><body>
<header><h1>Street Tacos in Holders — crop &amp; colour</h1>
<p class="sub"><code style="display:inline;color:#7fb2e8">{PID}</code> · 1440×2560 portrait, from <code style="display:inline;color:#7fb2e8">approved-assets/photos/promo</code>. The source is 9:16 and the email tile is 3:2, so it needs a hard crop. Colour correction applied: <code style="display:inline;color:#7fb2e8">{GRADE}</code> — the same grade used on the site's homepage hero.</p></header>
<h2>Colour correction — before / after</h2>
<p class="note">Both at the same crop, so the only difference is the grade.</p>
<div class="pair">
  <figure><img src="{B}/{UNGRADED}/{PID}" alt="Original"><figcaption><strong>Original</strong> — no correction</figcaption></figure>
  <figure><img src="{B}/{GRADE}/f_auto,q_auto:best,w_1200,h_800,c_fill,g_auto/{PID}" alt="Corrected"><figcaption><strong>Corrected</strong> — auto colour, vibrance 40, saturation 18, contrast 16, sharpen 35</figcaption></figure>
</div>
<h2>Crop options</h2>
<p class="note">All colour corrected. The email currently uses <strong>A</strong>.</p>
<div class="grid">{cards}</div>
</body></html>"""
open("image-crop-tacos.html","w").write(html)
open("_urls_crop.txt","w").write("\n".join([f"{B}/{t}/{PID}" for _,_,_,t,_ in VARIANTS]+[f"{B}/{UNGRADED}/{PID}"])+"\n")
print("wrote crop page")
