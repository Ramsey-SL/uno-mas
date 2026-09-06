from _shared import *
import json

CROP="f_auto,q_auto:best,w_1200,h_800,c_fill,g_auto,e_vibrance:22"
GRADE="e_auto_color,e_vibrance:40,e_saturation:18,e_contrast:16,e_sharpen:35/f_auto,q_auto:best,w_1200,h_800,c_fill,g_auto"
TR={"20260207_UM_PROMO_StreetTacosInHolders_FINAL":GRADE}
P=json.load(open("picks.json"))
def im(k): 
    pid=P[k]; return f"{B}/{TR.get(pid,CROP)}/{pid}"

GOLD="#C79A16"
ITEMS=[
 dict(k="sat", meta="Now through Sunday 4pm", kicker="Ends Sunday at 4pm", color=PINK,
      title="2 House Margs<br>+ Chips &amp; Dip", flat="2 House Margs + Chips &amp; Dip", price="$25", alt="Chips and dip",
      blurb="Two house margaritas and chips with your choice of salsa, guac, or queso. Running all day, every day we're open — right through Sunday. Then it's gone.",
      cta=("See what else is on", SITE)),
 dict(k="fri", meta="Friday &amp; Saturday · 8–10pm", kicker="New · Friday &amp; Saturday", color=BLUE,
      title="Late Night<br>Happy Hour", flat="Late Night Happy Hour", price="$10", alt="Street tacos",
      blurb="Pick any two street tacos for $10 — carne asada, al pastor chicken, carnitas, barbacoa, batata, hongos. House margs $6, pints $5, shots $4, marg pitchers $30. Both nights, 8–10pm.",
      cta=("See the late night menu", SITE+"/menu?tab=late-night")),
 dict(k="sun", meta="Sunday · 10am–4pm", kicker="Sundays · 10am–4pm", color=GOLD,
      title="Sunday Brunch", flat="Sunday Brunch", price="", alt="Churro french toast",
      blurb="Churro french toast, birria, and margaritas that start at 10am. Our busiest service of the week — a reservation is the move. And the $25 marg deal ends when we close at 4pm.",
      cta=("Reserve a table", SITE+"/reservations")),
]

HERO = f"""
  <tr><td style="padding:34px 40px 0;text-align:center;">
    <img src="{IMG['logo_n']}" width="150" alt="Uno Más" style="width:150px;margin:0 auto;"></td></tr>
  <tr><td class="px" style="padding:44px 40px 40px;text-align:center;">
    <p style="margin:0 0 16px;font-family:{Bo};font-size:12px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:{PINK};">This weekend at Uno Más</p>
    <h1 class="h1" style="margin:0 0 18px;font-family:{H};font-size:56px;line-height:52px;font-weight:700;text-transform:uppercase;color:{NAVY};letter-spacing:-.015em;">Three things<br>worth showing<br>up for.</h1>
    <p style="margin:0 auto;max-width:390px;font-family:{Bo};font-size:16px;line-height:27px;color:#6b6b6b;">One runs all weekend and then disappears. One's brand new. One's Sunday. All of it on North Monroe.</p>
  </td></tr>"""

SIGNOFF = f"""
  <tr><td class="px" style="padding:6px 40px 48px;text-align:center;">
    <div style="height:1px;background:#E4E4E0;margin:0 0 32px;"></div>
    <p style="margin:0 0 8px;font-family:{H};font-size:36px;line-height:36px;font-weight:700;text-transform:uppercase;color:{NAVY};">Get a little lost.</p>
    <p style="margin:0;font-family:{Bo};font-size:14px;line-height:24px;color:#8a8a8a;">2020 N Monroe St, Suite C · Spokane</p>
  </td></tr>"""

def shell(inner):
    return f"""<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#FAFAF8;"><tr><td align="center" style="padding:0 0 20px;">
<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" style="width:600px;max-width:600px;background:#FAFAF8;">
{HERO}{inner}{SIGNOFF}{footer('#F0EFEB',NAVY,'#8a8a8a',IMG['logo_n'],'#d5d4cf')}
</table></td></tr></table>"""

ul = lambda href,label,c=NAVY: f'<a href="{href}" style="display:inline-block;font-family:{Bo};font-size:14px;font-weight:700;color:{c};border-bottom:2px solid {c};padding-bottom:3px;">{label} &nbsp;→</a>'
pill = lambda href,label,bg,fg: f'<table role="presentation" cellpadding="0" cellspacing="0"><tr><td style="background:{bg};border-radius:999px;"><a href="{href}" style="display:inline-block;padding:13px 28px;font-family:{Bo};font-size:13px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:{fg};">{label}</a></td></tr></table>'

# ---------- A · Full-bleed stack ----------
rows=""
for n,it in enumerate(ITEMS,1):
    price=f'<p style="margin:0 0 14px;font-family:{H};font-size:58px;line-height:50px;font-weight:700;color:{it["color"]};">{it["price"]}</p>' if it["price"] else ''
    rows+=f"""
  <tr><td style="padding:0;"><img src="{im(it['k'])}" width="600" alt="{it['alt']}" style="width:100%;max-width:600px;"></td></tr>
  <tr><td class="px" style="padding:30px 44px 42px;text-align:center;background:#fff;">
    <p style="margin:0 0 10px;font-family:{H};font-size:34px;line-height:32px;font-weight:700;color:{it['color']};">0{n}</p>
    <p style="margin:0 0 12px;font-family:{Bo};font-size:11px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:#9a9a96;">{it['meta']}</p>
    <h2 class="h2" style="margin:0 0 14px;font-family:{H};font-size:42px;line-height:38px;font-weight:700;text-transform:uppercase;color:{NAVY};">{it['title']}</h2>
    {price}
    <p style="margin:0 auto 24px;max-width:420px;font-family:{Bo};font-size:15px;line-height:26px;color:#6b6b6b;">{it['blurb']}</p>
    {pill(it['cta'][1],it['cta'][0],it['color'],'#fff' if it['color']!=YEL else NAVY)}
  </td></tr>
  <tr><td style="height:14px;background:#FAFAF8;"></td></tr>"""
open("mockup-7-fullbleed.html","w").write(page("Uno Más — Three things worth showing up for",
 "Margs + chips through Sunday, new Late Night Happy Hour, Sunday brunch.", shell(rows), "#FAFAF8"))

# ---------- B · Alternating split ----------
rows=""
for n,it in enumerate(ITEMS):
    img=f'<td class="stack" width="228" style="padding:0;"><img src="{im(it["k"])}" width="228" alt="{it["alt"]}" style="width:228px;max-width:228px;height:auto;"></td>'
    price=f'<p style="margin:0 0 10px;font-family:{H};font-size:44px;line-height:38px;font-weight:700;color:{it["color"]};">{it["price"]}</p>' if it["price"] else ''
    txt=f"""<td class="stack" style="padding:24px 24px 26px;vertical-align:top;">
      <p style="margin:0 0 9px;font-family:{Bo};font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{it['color']};">{it['meta']}</p>
      <h2 style="margin:0 0 10px;font-family:{H};font-size:30px;line-height:28px;font-weight:700;text-transform:uppercase;color:{NAVY};">{it['title']}</h2>
      {price}
      <p style="margin:0 0 16px;font-family:{Bo};font-size:13.5px;line-height:23px;color:#6b6b6b;">{it['blurb']}</p>
      {ul(it['cta'][1],it['cta'][0])}</td>"""
    cells = img+txt if n%2==0 else txt+img
    rows+=f"""
  <tr><td class="px" style="padding:0 40px 20px;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#fff;border:1px solid #ECECEC;border-radius:14px;overflow:hidden;">
      <tr>{cells}</tr></table></td></tr>"""
open("mockup-8-split.html","w").write(page("Uno Más — Three things worth showing up for",
 "Margs + chips through Sunday, new Late Night Happy Hour, Sunday brunch.", shell(rows), "#FAFAF8"))

# ---------- C · Poster bands, type over image ----------
rows=""
for it in ITEMS:
    price=f'<span style="font-family:{H};font-size:82px;line-height:68px;font-weight:700;color:{YEL};display:block;margin:0 0 8px;">{it["price"]}</span>' if it["price"] else ''
    rows+=f"""
  <tr><td class="px" style="padding:0 30px 20px;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-radius:14px;overflow:hidden;background:#0E1116;">
      <tr><td background="{im(it['k'])}" style="background-image:url('{im(it['k'])}');background-size:cover;background-position:center;padding:0;">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td style="padding:120px 0 0;"></td></tr></table>
      </td></tr>
      <tr><td style="padding:26px 26px 30px;text-align:center;background:#0E1116;">
        <p style="margin:0 0 10px;font-family:{Bo};font-size:11px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:{it['color']};">{it['meta']}</p>
        <h2 class="h2" style="margin:0 0 12px;font-family:{H};font-size:40px;line-height:36px;font-weight:700;text-transform:uppercase;color:#fff;">{it['title']}</h2>
        {price}
        <p style="margin:0 auto 22px;max-width:400px;font-family:{Bo};font-size:14px;line-height:24px;color:#9aa4b2;">{it['blurb']}</p>
        {pill(it['cta'][1],it['cta'][0],it['color'],'#fff')}
      </td></tr></table></td></tr>"""
open("mockup-9-poster.html","w").write(page("Uno Más — Three things worth showing up for",
 "Margs + chips through Sunday, new Late Night Happy Hour, Sunday brunch.", shell(rows), "#FAFAF8"))
print("wrote 7, 8, 9")
