from _shared import *

btn = lambda href,label,bg,fg: f"""<table role="presentation" cellpadding="0" cellspacing="0" style="margin:0 auto;"><tr><td style="background:{bg};border-radius:999px;"><a href="{href}" style="display:inline-block;padding:15px 34px;font-family:{Bo};font-size:14px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:{fg};">{label}</a></td></tr></table>"""

body = f"""
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#F6F4EE;"><tr><td align="center" style="padding:0 0 40px;">
<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" style="width:600px;max-width:600px;background:#FFFDF7;">

  <tr><td style="background:{NAVY};padding:22px 32px;text-align:center;">
    <img src="{IMG['logo_w']}" width="168" alt="Uno Más" style="width:168px;margin:0 auto;">
  </td></tr>

  <tr><td style="background:{PINK};padding:11px 20px;text-align:center;">
    <p style="margin:0;font-family:{Bo};font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#fff;">Your weekend, handled</p>
  </td></tr>

  <tr><td class="px" style="padding:44px 44px 8px;text-align:center;">
    <p style="margin:0 0 14px;font-family:{Bo};font-size:12px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:{BLUE};">Friday · Saturday · Sunday</p>
    <h1 class="h1" style="margin:0 0 18px;font-family:{H};font-size:58px;line-height:54px;font-weight:700;text-transform:uppercase;color:{NAVY};letter-spacing:-.01em;">Three good<br>reasons to<br>get a little lost.</h1>
    <p style="margin:0 auto;max-width:400px;font-family:{Bo};font-size:16px;line-height:26px;color:#4a4a4a;">One's ending Sunday. One's brand new. One's the best hour of the weekend. Pick all three — we won't judge.</p>
  </td></tr>

  <tr><td style="padding:34px 0 0;"><div style="height:1px;background:#E8E2D6;margin:0 44px;"></div></td></tr>

  <!-- 01 $25 -->
  <tr><td class="px" style="padding:36px 44px 0;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
      <td style="font-family:{H};font-size:46px;line-height:40px;color:{PINK};font-weight:700;width:70px;vertical-align:top;">01</td>
      <td style="vertical-align:top;">
        <p style="margin:0 0 6px;font-family:{Bo};font-size:11px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:#9a9a9a;">Ends Sunday at 4pm</p>
        <h2 class="h2" style="margin:0 0 10px;font-family:{H};font-size:36px;line-height:34px;font-weight:700;text-transform:uppercase;color:{NAVY};">2 House Margs<br>+ Chips &amp; Dip</h2>
      </td>
    </tr></table>
  </td></tr>
  <tr><td class="px" style="padding:18px 44px 0;">
    <img src="{IMG['flat']}" width="512" alt="Street tacos and a house margarita" style="width:100%;max-width:512px;border-radius:4px;">
  </td></tr>
  <tr><td class="px" style="padding:22px 44px 0;text-align:center;">
    <table role="presentation" cellpadding="0" cellspacing="0" style="margin:0 auto;"><tr>
      <td style="background:{YEL};padding:14px 30px;">
        <span style="font-family:{H};font-size:62px;line-height:52px;font-weight:700;color:{NAVY};">$25</span>
      </td></tr></table>
    <p style="margin:18px 0 0;font-family:{Bo};font-size:15px;line-height:25px;color:#4a4a4a;">Two house margaritas and your choice of chips &amp; dip —<br><strong style="color:{NAVY};">salsa, guac, or queso</strong>. All day, right through Sunday.</p>
  </td></tr>

  <tr><td style="padding:34px 0 0;"><div style="height:1px;background:#E8E2D6;margin:0 44px;"></div></td></tr>

  <!-- 02 late night -->
  <tr><td class="px" style="padding:36px 44px 0;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
      <td style="font-family:{H};font-size:46px;line-height:40px;color:{BLUE};font-weight:700;width:70px;vertical-align:top;">02</td>
      <td style="vertical-align:top;">
        <p style="margin:0 0 6px;font-family:{Bo};font-size:11px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:#9a9a9a;">New · Fri &amp; Sat, 8–10pm</p>
        <h2 class="h2" style="margin:0 0 10px;font-family:{H};font-size:36px;line-height:34px;font-weight:700;text-transform:uppercase;color:{NAVY};">Late Night<br>Happy Hour</h2>
      </td>
    </tr></table>
  </td></tr>
  <tr><td class="px" style="padding:18px 44px 0;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#0E1116;border-radius:4px;">
      <tr><td style="padding:0;">
        <img src="{IMG['tacos2']}" width="512" alt="Two street tacos" style="width:100%;max-width:512px;border-radius:4px 4px 0 0;">
      </td></tr>
      <tr><td style="padding:26px 28px 28px;text-align:center;">
        <p style="margin:0 0 4px;font-family:{Bo};font-size:11px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:{BLUE};">Pick any two street tacos</p>
        <p style="margin:0 0 16px;font-family:{H};font-size:56px;line-height:50px;font-weight:700;color:{YEL};">$10</p>
        <p style="margin:0 0 20px;font-family:{Bo};font-size:13px;line-height:24px;color:#cfd4da;">Carne Asada · Al Pastor Chicken · Carnitas<br>Barbacoa · Batata · Hongos</p>
        <div style="height:1px;background:#2a2f38;margin:0 0 18px;"></div>
        <p style="margin:0;font-family:{Bo};font-size:14px;line-height:26px;color:#fff;font-weight:600;">
          House Margs <span style="color:{PINK};">$6</span> &nbsp;·&nbsp; Pints <span style="color:{PINK};">$5</span><br>
          Shots <span style="color:{PINK};">$4</span> &nbsp;·&nbsp; Marg Pitchers <span style="color:{PINK};">$30</span>
        </p>
      </td></tr>
    </table>
  </td></tr>
  <tr><td class="px" style="padding:20px 44px 0;text-align:center;">{btn(SITE+'/menu?tab=late-night','See the late night menu',NAVY,'#fff')}</td></tr>

  <tr><td style="padding:34px 0 0;"><div style="height:1px;background:#E8E2D6;margin:0 44px;"></div></td></tr>

  <!-- 03 brunch -->
  <tr><td class="px" style="padding:36px 44px 0;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
      <td style="font-family:{H};font-size:46px;line-height:40px;color:{YEL};font-weight:700;width:70px;vertical-align:top;text-shadow:0 1px 0 #d9c800;">03</td>
      <td style="vertical-align:top;">
        <p style="margin:0 0 6px;font-family:{Bo};font-size:11px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:#9a9a9a;">Sundays · 10am–4pm</p>
        <h2 class="h2" style="margin:0 0 10px;font-family:{H};font-size:36px;line-height:34px;font-weight:700;text-transform:uppercase;color:{NAVY};">Sunday Brunch</h2>
      </td>
    </tr></table>
  </td></tr>
  <tr><td class="px" style="padding:18px 44px 0;">
    <img src="{IMG['brunch']}" width="512" alt="Churro french toast" style="width:100%;max-width:512px;border-radius:4px;">
  </td></tr>
  <tr><td class="px" style="padding:20px 44px 0;text-align:center;">
    <p style="margin:0 0 20px;font-family:{Bo};font-size:15px;line-height:25px;color:#4a4a4a;">Churro french toast. Birria. Margaritas before noon, which is<br>legal on Sundays. Tables go fast — book ahead.</p>
    {btn(SITE+'/reservations','Reserve a table',PINK,'#fff')}
  </td></tr>

  <tr><td class="px" style="padding:44px 44px 40px;text-align:center;">
    <p style="margin:0;font-family:{H};font-size:34px;line-height:34px;font-weight:700;text-transform:uppercase;color:{NAVY};">Get a little lost.</p>
  </td></tr>

  {footer(NAVY,'#ffffff','#93a7bd',IMG['logo_w'],'#38536e')}

</table></td></tr></table>"""

open("mockup-1-weekend-lineup.html","w").write(page(
 "Uno Más — The Weekend Lineup",
 "Margs + chips for $25 (ends Sunday), new Late Night Happy Hour, and Sunday brunch.", body, "#F6F4EE"))
print("wrote 1")
