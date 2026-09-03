from _shared import *
btn = lambda href,label,bg,fg: f"""<table role="presentation" cellpadding="0" cellspacing="0"><tr><td style="background:{bg};border-radius:999px;"><a href="{href}" style="display:inline-block;padding:13px 28px;font-family:{Bo};font-size:13px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:{fg};">{label}</a></td></tr></table>"""

def stop(day, date, dotclr, time, title, img, alt, lines, cta, last=False):
    rule = '' if last else f'<div style="width:2px;background:#E2E0DA;height:100%;min-height:40px;margin:0 auto;"></div>'
    return f"""
  <tr><td class="px" style="padding:0 40px;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
      <td width="58" style="vertical-align:top;text-align:center;padding:0 14px 0 0;">
        <div style="width:16px;height:16px;border-radius:50%;background:{dotclr};margin:6px auto 8px;"></div>
        {rule}
      </td>
      <td style="vertical-align:top;padding:0 0 34px;">
        <p style="margin:0 0 2px;font-family:{H};font-size:30px;line-height:28px;font-weight:700;text-transform:uppercase;color:{NAVY};">{day}</p>
        <p style="margin:0 0 14px;font-family:{Bo};font-size:12px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:{dotclr};">{date} &nbsp;·&nbsp; {time}</p>
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#fff;border-radius:12px;overflow:hidden;border:1px solid #EDEBE4;">
          <tr><td style="padding:0;"><img src="{img}" width="440" alt="{alt}" style="width:100%;max-width:440px;"></td></tr>
          <tr><td style="padding:22px 22px 24px;">
            <h3 style="margin:0 0 12px;font-family:{H};font-size:30px;line-height:28px;font-weight:700;text-transform:uppercase;color:{NAVY};">{title}</h3>
            <p style="margin:0 0 18px;font-family:{Bo};font-size:14px;line-height:25px;color:#6b6b6b;">{lines}</p>
            {cta}
          </td></tr>
        </table>
      </td>
    </tr></table>
  </td></tr>"""

body = f"""
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#F4F2EC;"><tr><td align="center" style="padding:0 0 30px;">
<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" style="width:600px;max-width:600px;background:#F4F2EC;">

  <tr><td style="background:{NAVY};padding:26px 32px;text-align:center;">
    <img src="{IMG['logo_w']}" width="156" alt="Uno Más" style="width:156px;margin:0 auto;">
  </td></tr>

  <tr><td class="px" style="padding:42px 40px 36px;text-align:center;">
    <p style="margin:0 0 14px;font-family:{Bo};font-size:12px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:{PINK};">Sept 4 – 7 · North Monroe</p>
    <h1 class="h1" style="margin:0 0 16px;font-family:{H};font-size:60px;line-height:54px;font-weight:700;text-transform:uppercase;color:{NAVY};letter-spacing:-.015em;">Your weekend,<br>already planned.</h1>
    <p style="margin:0 auto;max-width:390px;font-family:{Bo};font-size:16px;line-height:27px;color:#6b6b6b;">You just have to show up. Here's how the next three days look at Uno Más.</p>
  </td></tr>

  {stop('Friday','Sept 4',BLUE,'8–10pm','Late Night<br>Happy Hour',IMG['tacos2'],'Two street tacos',
    'Pick <strong style="color:'+NAVY+';">any two street tacos for $10</strong> — carne asada, al pastor chicken, carnitas, barbacoa, batata, hongos.<br><br>House margs $6 · Pints $5 · Shots $4 · Marg pitchers $30',
    btn(SITE+'/menu?tab=late-night','See the menu',NAVY,'#fff'))}

  {stop('Saturday','Sept 5',PINK,'All day + 8–10pm','Margs, chips,<br>and one more night',IMG['flat'],'Street tacos and a margarita',
    '<strong style="color:'+NAVY+';">2 house margs + chips &amp; dip — $25.</strong> Salsa, guac, or queso. All day long.<br><br>Then Late Night Happy Hour runs again 8–10pm. Two good reasons, one day.',
    btn(SITE,'Plan your visit',PINK,'#fff'))}

  {stop('Sunday','Sept 6','#C79A16','10am–4pm','Brunch —<br>and last call',IMG['brunch'],'Churro french toast',
    'Churro french toast, birria, margaritas before noon. Our busiest service of the week, so book ahead.<br><br><strong style="color:'+NAVY+';">The $25 marg deal ends when we close at 4pm.</strong>',
    btn(SITE+'/reservations','Reserve a table',NAVY,'#fff'), last=True)}

  <tr><td class="px" style="padding:6px 40px 44px;text-align:center;">
    <div style="height:1px;background:#E2E0DA;margin:0 0 30px;"></div>
    <p style="margin:0 0 10px;font-family:{H};font-size:38px;line-height:36px;font-weight:700;text-transform:uppercase;color:{PINK};">Get a little lost.</p>
    <p style="margin:0;font-family:{Bo};font-size:14px;line-height:24px;color:#8a8a8a;">2020 N Monroe St, Suite C · Spokane, WA</p>
  </td></tr>

  {footer(NAVY,'#ffffff','#93a7bd',IMG['logo_w'],'#38536e')}

</table></td></tr></table>"""

open("mockup-5-weekend-itinerary.html","w").write(page(
 "Uno Más — Your weekend, already planned",
 "Friday late night, Saturday margs, Sunday brunch. The $25 deal ends at 4pm Sunday.", body, "#F4F2EC"))
print("wrote 5")
