from _shared import *
import sys, json

CROP = "f_auto,q_auto:best,w_1200,h_800,c_fill,g_auto,e_vibrance:22"
# Per-asset overrides. The street-taco holders shot is a tall 9:16 original that
# needs the site's colour-correction grade, so it gets its own transform.
GRADE = "e_auto_color,e_vibrance:40,e_saturation:18,e_contrast:16,e_sharpen:35/f_auto,q_auto:best,w_1200,h_800,c_fill,g_auto"
TRANSFORMS = {"20260207_UM_PROMO_StreetTacosInHolders_FINAL": GRADE}
def im(pid): return f"{B}/{TRANSFORMS.get(pid, CROP)}/{pid}"

# Defaults = my picks. Override via picks.json to re-render with different images.
PICKS = {"fri":"uno-mas/approved-assets/photos/food/20260724_UM_FOOD_StreetTaco_v3",
         "sat":"uno-mas/approved-assets/photos/food/20260814_UM_FOOD_ChipsGuacTrio_v1",
         "sun":"uno-mas/approved-assets/photos/brunch/20260724_UM_BRUNCH_FrenchToastPrep_v3"}
try: PICKS.update(json.load(open("picks.json")))
except Exception: pass

link = lambda href,label: f'<a href="{href}" style="display:inline-block;font-family:{Bo};font-size:14px;font-weight:700;color:{NAVY};letter-spacing:.02em;border-bottom:2px solid {NAVY};padding-bottom:3px;">{label} &nbsp;→</a>'

def stop(day, date, dot, time, kicker, kcolor, title, price, pricecolor, img, alt, blurb, cta, last=False):
    meta = " &nbsp;·&nbsp; ".join(x for x in (date, time) if x)
    rule = '' if last else '<div style="width:2px;background:#E4E4E0;height:100%;min-height:60px;margin:0 auto;"></div>'
    priceblock = f'<p style="margin:0 0 14px;font-family:{H};font-size:52px;line-height:46px;font-weight:700;color:{pricecolor};">{price}</p>' if price else ''
    return f"""
  <tr><td class="px" style="padding:0 40px;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
      <td width="56" style="vertical-align:top;text-align:center;padding:0 16px 0 0;">
        <div style="width:14px;height:14px;border-radius:50%;background:{dot};margin:8px auto 8px;"></div>
        {rule}
      </td>
      <td style="vertical-align:top;padding:0 0 36px;">
        <p style="margin:0 0 3px;font-family:{H};font-size:28px;line-height:26px;font-weight:700;text-transform:uppercase;color:{NAVY};">{day}</p>
        <p style="margin:0 0 16px;font-family:{Bo};font-size:12px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:#9a9a96;">{meta}</p>
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#fff;border:1px solid #ECECEC;border-radius:14px;overflow:hidden;">
          <tr><td style="padding:0;"><img src="{img}" width="446" alt="{alt}" style="width:100%;max-width:446px;"></td></tr>
          <tr><td style="padding:28px 28px 30px;">
            <p style="margin:0 0 12px;font-family:{Bo};font-size:11px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:{kcolor};">{kicker}</p>
            <h2 class="h2" style="margin:0 0 14px;font-family:{H};font-size:36px;line-height:34px;font-weight:700;text-transform:uppercase;color:{NAVY};letter-spacing:-.01em;">{title}</h2>
            {priceblock}
            <p style="margin:0 0 22px;font-family:{Bo};font-size:15px;line-height:26px;color:#6b6b6b;">{blurb}</p>
            {cta}
          </td></tr>
        </table>
      </td>
    </tr></table>
  </td></tr>"""

body = f"""
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#FAFAF8;"><tr><td align="center" style="padding:0 0 20px;">
<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" style="width:600px;max-width:600px;background:#FAFAF8;">

  <tr><td style="padding:34px 40px 0;text-align:center;">
    <img src="{IMG['logo_n']}" width="150" alt="Uno Más" style="width:150px;margin:0 auto;">
  </td></tr>

  <tr><td class="px" style="padding:44px 40px 42px;text-align:center;">
    <p style="margin:0 0 16px;font-family:{Bo};font-size:12px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:{PINK};">This weekend at Uno Más</p>
    <h1 class="h1" style="margin:0 0 18px;font-family:{H};font-size:56px;line-height:52px;font-weight:700;text-transform:uppercase;color:{NAVY};letter-spacing:-.015em;">Three things<br>worth showing<br>up for.</h1>
    <p style="margin:0 auto;max-width:380px;font-family:{Bo};font-size:16px;line-height:27px;color:#6b6b6b;">One runs all weekend and then disappears. One's brand new. One's Sunday. All of it on North Monroe.</p>
  </td></tr>

  {stop('All Weekend','Now through Sunday 4pm',PINK,'','Ends Sunday at 4pm',PINK,'2 House Margs<br>+ Chips &amp; Dip','$25',PINK,
    im(PICKS['sat']),'Chips and dip',
    'Two house margaritas and chips with your choice of salsa, guac, or queso. Running all day, every day we\'re open — right through Sunday. Then it\'s gone.',
    link(SITE,'See what else is on'))}

  {stop('Fri &amp; Sat','Sept 4 &amp; 5',BLUE,'8–10pm','New · Friday &amp; Saturday',BLUE,'Late Night<br>Happy Hour','$10',BLUE,
    im(PICKS['fri']),'Street tacos',
    'Pick any two street tacos for $10 — carne asada, al pastor chicken, carnitas, barbacoa, batata, hongos. House margs $6, pints $5, shots $4, marg pitchers $30. Both nights, 8–10pm.',
    link(SITE+'/menu?tab=late-night','See the late night menu'))}

  {stop('Sunday','Sept 6','#C79A16','10am–4pm','Sundays · 10am–4pm','#C79A16','Sunday Brunch','','',
    im(PICKS['sun']),'Churro french toast',
    'Churro french toast, birria, and margaritas that start at 10am. Our busiest service of the week — a reservation is the move. And the $25 marg deal ends when we close at 4pm.',
    link(SITE+'/reservations','Reserve a table'), last=True)}

  <tr><td class="px" style="padding:6px 40px 48px;text-align:center;">
    <div style="height:1px;background:#E4E4E0;margin:0 0 32px;"></div>
    <p style="margin:0 0 8px;font-family:{H};font-size:36px;line-height:36px;font-weight:700;text-transform:uppercase;color:{NAVY};">Get a little lost.</p>
    <p style="margin:0;font-family:{Bo};font-size:14px;line-height:24px;color:#8a8a8a;">2020 N Monroe St, Suite C · Spokane</p>
  </td></tr>

  {footer('#F0EFEB',NAVY,'#8a8a8a',IMG['logo_n'],'#d5d4cf')}

</table></td></tr></table>"""

open("mockup-6-hybrid.html","w").write(page(
 "Uno Más — Three things worth showing up for",
 "Friday late night, Saturday margs, Sunday brunch. The $25 deal ends at 4pm Sunday.", body, "#FAFAF8"))
print("wrote hybrid with:", json.dumps(PICKS, indent=1))
