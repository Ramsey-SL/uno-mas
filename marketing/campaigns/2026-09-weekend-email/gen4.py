from _shared import *
btn = lambda href,label,c: f"""<a href="{href}" style="display:inline-block;font-family:{Bo};font-size:14px;font-weight:700;color:{c};letter-spacing:.02em;border-bottom:2px solid {c};padding-bottom:3px;">{label} &nbsp;→</a>"""

def card(img, alt, kicker, kcolor, title, price, priceclr, blurb, cta_href, cta_label):
    return f"""
  <tr><td class="px" style="padding:0 40px 46px;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#fff;border:1px solid #ECECEC;border-radius:14px;overflow:hidden;">
      <tr><td style="padding:0;"><img src="{img}" width="518" alt="{alt}" style="width:100%;max-width:518px;"></td></tr>
      <tr><td style="padding:30px 30px 32px;">
        <p style="margin:0 0 12px;font-family:{Bo};font-size:11px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:{kcolor};">{kicker}</p>
        <h2 class="h2" style="margin:0 0 14px;font-family:{H};font-size:38px;line-height:36px;font-weight:700;text-transform:uppercase;color:{NAVY};letter-spacing:-.01em;">{title}</h2>
        {price and f'<p style="margin:0 0 14px;font-family:{H};font-size:52px;line-height:46px;font-weight:700;color:{priceclr};">{price}</p>' or ''}
        <p style="margin:0 0 22px;font-family:{Bo};font-size:15px;line-height:26px;color:#6b6b6b;">{blurb}</p>
        {btn(cta_href, cta_label, NAVY)}
      </td></tr>
    </table>
  </td></tr>"""

body = f"""
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#FAFAF8;"><tr><td align="center" style="padding:0 0 20px;">
<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" style="width:600px;max-width:600px;background:#FAFAF8;">

  <tr><td style="padding:34px 40px 0;text-align:center;">
    <img src="{IMG['logo_n']}" width="150" alt="Uno Más" style="width:150px;margin:0 auto;">
  </td></tr>

  <tr><td class="px" style="padding:44px 40px 40px;text-align:center;">
    <p style="margin:0 0 16px;font-family:{Bo};font-size:12px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:{PINK};">This weekend at Uno Más</p>
    <h1 class="h1" style="margin:0 0 18px;font-family:{H};font-size:56px;line-height:52px;font-weight:700;text-transform:uppercase;color:{NAVY};letter-spacing:-.015em;">Three things<br>worth showing<br>up for.</h1>
    <p style="margin:0 auto;max-width:380px;font-family:{Bo};font-size:16px;line-height:27px;color:#6b6b6b;">Friday through Sunday on North Monroe. One of them disappears at 4pm Sunday.</p>
  </td></tr>

  {card(IMG['flat'],'Street tacos and a house margarita','Ends Sunday at 4pm',PINK,'2 House Margs<br>+ Chips &amp; Dip','$25',PINK,'Two house margaritas and chips with your choice of salsa, guac, or queso. Available all day — but only through Sunday.',SITE,'See what else is on')}

  {card(IMG['tacos2'],'Two street tacos','New · Fri &amp; Sat, 8–10pm',BLUE,'Late Night<br>Happy Hour','$10',BLUE,'Pick any two street tacos for $10 — carne asada, al pastor chicken, carnitas, barbacoa, batata, hongos. House margs $6, pints $5, shots $4, pitchers $30.',SITE+'/menu?tab=late-night','See the late night menu')}

  {card(IMG['brunch'],'Churro french toast','Sundays · 10am–4pm','#C79A16','Sunday Brunch','',NAVY,'Churro french toast, birria, and margaritas that start at 10am. Our busiest service of the week — a reservation is the move.',SITE+'/reservations','Reserve a table')}

  <tr><td class="px" style="padding:8px 40px 48px;text-align:center;">
    <div style="height:1px;background:#E4E4E0;margin:0 0 32px;"></div>
    <p style="margin:0 0 8px;font-family:{H};font-size:36px;line-height:36px;font-weight:700;text-transform:uppercase;color:{NAVY};">Get a little lost.</p>
    <p style="margin:0;font-family:{Bo};font-size:14px;line-height:24px;color:#8a8a8a;">2020 N Monroe St, Suite C · Spokane</p>
  </td></tr>

  {footer('#F0EFEB',NAVY,'#8a8a8a',IMG['logo_n'],'#d5d4cf')}

</table></td></tr></table>"""

open("mockup-4-three-cards.html","w").write(page(
 "Uno Más — Three things worth showing up for",
 "$25 margs + chips ends Sunday · New Late Night Happy Hour · Sunday brunch reservations.", body, "#FAFAF8"))
print("wrote 4")
