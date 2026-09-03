from _shared import *
import json
GOLD="#C79A16"; INK="#0E1116"
# 4:3 instead of 3:2 — taller frame, so each photo occupies more vertical space too.
CROP="f_auto,q_auto:best,w_1200,h_900,c_fill,g_auto,e_vibrance:22"
GRADE="e_auto_color,e_vibrance:40,e_saturation:18,e_contrast:16,e_sharpen:35/f_auto,q_auto:best,w_1200,h_900,c_fill,g_auto"
TR={"20260207_UM_PROMO_StreetTacosInHolders_FINAL":GRADE}
P=json.load(open("picks.json"))
def im(k):
    pid=P[k]; return f"{B}/{TR.get(pid,CROP)}/{pid}"

ITEMS=[
 dict(k="sat", meta="Now through Sunday 4pm", color=PINK, title="2 House Margs<br>+ Chips &amp; Dip", price="$25", alt="Chips and dip",
      blurb="Two house margaritas and chips with your choice of salsa, guac, or queso. Running all day, every day we're open — right through Sunday.",
      cta=("See what else is on", SITE)),
 dict(k="fri", meta="Friday &amp; Saturday · 8–10pm", color=BLUE, title="Late Night<br>Happy Hour", price="$10", alt="Street tacos",
      blurb="Pick any two street tacos for $10 — carne asada, al pastor chicken, carnitas, barbacoa, batata, hongos.", blurb2="House margs $6 &nbsp;·&nbsp; Pints $5 &nbsp;·&nbsp; Shots $4 &nbsp;·&nbsp; Marg pitchers $30. Both nights, 8–10pm.",
      cta=("See the late night menu", SITE+"/menu?tab=late-night")),
 dict(k="sun", meta="Sunday · 10am–4pm", color=GOLD, title="Sunday Brunch", price="", alt="Churro french toast",
      blurb="Churro french toast, birria, and margaritas that start at 10am. Our busiest service of the week — a reservation is the move.",
      cta=("Reserve a table", SITE+"/reservations")),
]

HERO=f"""
  <tr><td style="padding:34px 40px 0;text-align:center;">
    <img src="{IMG['logo_n']}" width="150" alt="Uno Más" style="width:150px;margin:0 auto;"></td></tr>
  <tr><td class="px" style="padding:44px 40px 40px;text-align:center;">
    <p style="margin:0 0 16px;font-family:{Bo};font-size:12px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:{PINK};">This weekend at Uno Más</p>
    <h1 class="h1" style="margin:0 0 18px;font-family:{H};font-size:56px;line-height:52px;font-weight:700;text-transform:uppercase;color:{NAVY};letter-spacing:-.015em;">Three things<br>worth showing<br>up for.</h1>
    <p style="margin:0 auto;max-width:390px;font-family:{Bo};font-size:16px;line-height:27px;color:#6b6b6b;">One runs all weekend and then disappears. One's brand new. One's Sunday. All of it on North Monroe.</p>
  </td></tr>"""
SIGNOFF=f"""
  <tr><td class="px" style="padding:22px 40px 48px;text-align:center;">
    <div style="height:1px;background:#E4E4E0;margin:0 0 32px;"></div>
    <p style="margin:0 0 8px;font-family:{H};font-size:36px;line-height:36px;font-weight:700;text-transform:uppercase;color:{NAVY};">Get a little lost.</p>
    <p style="margin:0;font-family:{Bo};font-size:14px;line-height:24px;color:#8a8a8a;">2020 N Monroe St, Suite C · Spokane</p>
  </td></tr>"""
pill=lambda href,label,bg,fg: f'<table role="presentation" cellpadding="0" cellspacing="0" style="margin:0 auto;"><tr><td style="background:{bg};border-radius:999px;"><a href="{href}" style="display:inline-block;padding:14px 30px;font-family:{Bo};font-size:13px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:{fg};">{label}</a></td></tr></table>'

def build(pad, imgw, radius, label):
    rows=""
    for it in ITEMS:
        price=f'<p style="margin:0 0 12px;font-family:{H};font-size:92px;line-height:76px;font-weight:700;color:{YEL};">{it["price"]}</p>' if it["price"] else ''
        r = f"border-radius:{radius}px;overflow:hidden;" if radius else ""
        rows+=f"""
  <tr><td class="px" style="padding:0 {pad}px 18px;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:{INK};{r}">
      <tr><td style="padding:0;font-size:0;line-height:0;">
        <img src="{im(it['k'])}" width="{imgw}" alt="{it['alt']}" style="width:100%;max-width:{imgw}px;display:block;">
      </td></tr>
      <tr><td style="padding:30px 26px 34px;text-align:center;">
        <p style="margin:0 0 12px;font-family:{Bo};font-size:11px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:{it['color']};">{it['meta']}</p>
        <h2 class="h2" style="margin:0 0 14px;font-family:{H};font-size:44px;line-height:40px;font-weight:700;text-transform:uppercase;color:#fff;">{it['title']}</h2>
        {price}
        <p style="margin:0 auto 14px;max-width:420px;font-family:{Bo};font-size:15px;line-height:25px;color:#9aa4b2;">{it['blurb']}</p>
        {f'<p style="margin:0 auto 24px;max-width:420px;font-family:{Bo};font-size:14px;line-height:24px;font-weight:600;color:#fff;">{it["blurb2"]}</p>' if it.get("blurb2") else '<div style="height:10px;line-height:10px;">&nbsp;</div>'}
        {pill(it['cta'][1],it['cta'][0],it['color'],'#fff')}
      </td></tr></table></td></tr>"""
    inner=f"""<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#FAFAF8;"><tr><td align="center" style="padding:0 0 20px;">
<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" style="width:600px;max-width:600px;background:#FAFAF8;">
{HERO}{rows}{SIGNOFF}{footer('#F0EFEB',NAVY,'#8a8a8a',IMG['logo_n'],'#d5d4cf')}
</table></td></tr></table>"""
    return page("Uno Más — Three things worth showing up for",
      "Margs + chips through Sunday, new Late Night Happy Hour, Sunday brunch.", inner, "#FAFAF8")

open("mockup-9-poster.html","w").write(build(14, 572, 14, "inset"))
open("mockup-9b-poster-fullbleed.html","w").write(build(0, 600, 0, "fullbleed"))
print("wrote 9 (572px, 4:3) and 9b (600px edge-to-edge)")
