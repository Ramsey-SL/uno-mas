from _shared import *
INK="#08090C"
btn = lambda href,label,bg,fg: f"""<table role="presentation" cellpadding="0" cellspacing="0" style="margin:0 auto;"><tr><td style="background:{bg};border-radius:2px;"><a href="{href}" style="display:inline-block;padding:16px 36px;font-family:{Bo};font-size:13px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:{fg};">{label}</a></td></tr></table>"""

body = f"""
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:{INK};"><tr><td align="center" style="padding:0;">
<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" style="width:600px;max-width:600px;background:{INK};">

  <tr><td style="padding:28px 32px;text-align:center;border-bottom:1px solid #1b1f27;">
    <img src="{IMG['logo_w']}" width="150" alt="Uno Más" style="width:150px;margin:0 auto;">
  </td></tr>

  <!-- HERO late night -->
  <tr><td style="position:relative;padding:0;">
    <img src="{IMG['tacos2']}" width="600" alt="Two street tacos" style="width:100%;max-width:600px;opacity:.62;">
  </td></tr>
  <tr><td class="px" style="padding:0 40px 0;background:{INK};">
    <div style="margin-top:-58px;position:relative;text-align:center;">
      <p style="margin:0 0 12px;font-family:{Bo};font-size:11px;font-weight:700;letter-spacing:.28em;text-transform:uppercase;color:{BLUE};">New · Fri &amp; Sat · 8–10pm</p>
      <h1 class="h1" style="margin:0 0 20px;font-family:{H};font-size:66px;line-height:58px;font-weight:700;text-transform:uppercase;color:#fff;letter-spacing:-.015em;">Late Night<br>Happy Hour</h1>
    </div>
  </td></tr>

  <tr><td class="px" style="padding:8px 40px 0;text-align:center;">
    <p style="margin:0 0 28px;font-family:{Bo};font-size:16px;line-height:27px;color:#9aa4b2;">The last two hours of the night just got a lot<br>more interesting. Every Friday and Saturday.</p>
  </td></tr>

  <tr><td class="px" style="padding:0 40px;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border:1px solid {BLUE};">
      <tr><td style="padding:30px 26px 26px;text-align:center;">
        <p style="margin:0 0 6px;font-family:{Bo};font-size:11px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:{BLUE};">Pick any two street tacos</p>
        <p style="margin:0 0 20px;font-family:{H};font-size:88px;line-height:74px;font-weight:700;color:{YEL};">$10</p>
        <p style="margin:0;font-family:{Bo};font-size:14px;line-height:28px;color:#e2e6eb;letter-spacing:.03em;">
          CARNE ASADA &nbsp;·&nbsp; BARBACOA<br>
          AL PASTOR CHICKEN &nbsp;·&nbsp; BATATA<br>
          CARNITAS &nbsp;·&nbsp; HONGOS
        </p>
      </td></tr>
      <tr><td style="padding:0 26px;"><div style="height:1px;background:{PINK};"></div></td></tr>
      <tr><td style="padding:24px 26px 30px;text-align:center;">
        <p style="margin:0 0 16px;font-family:{Bo};font-size:11px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:{PINK};">Drinks</p>
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
          <tr>
            <td class="stack" width="50%" style="padding:0 0 12px;text-align:center;">
              <span style="font-family:{H};font-size:38px;line-height:34px;font-weight:700;color:#fff;">$6</span>
              <p style="margin:4px 0 0;font-family:{Bo};font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:#8c96a4;">House Margs</p>
            </td>
            <td class="stack" width="50%" style="padding:0 0 12px;text-align:center;">
              <span style="font-family:{H};font-size:38px;line-height:34px;font-weight:700;color:#fff;">$5</span>
              <p style="margin:4px 0 0;font-family:{Bo};font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:#8c96a4;">Pints</p>
            </td>
          </tr>
          <tr>
            <td class="stack" width="50%" style="text-align:center;">
              <span style="font-family:{H};font-size:38px;line-height:34px;font-weight:700;color:#fff;">$4</span>
              <p style="margin:4px 0 0;font-family:{Bo};font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:#8c96a4;">Shots · well pours</p>
            </td>
            <td class="stack" width="50%" style="text-align:center;">
              <span style="font-family:{H};font-size:38px;line-height:34px;font-weight:700;color:#fff;">$30</span>
              <p style="margin:4px 0 0;font-family:{Bo};font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:#8c96a4;">Marg Pitchers</p>
            </td>
          </tr>
        </table>
      </td></tr>
    </table>
  </td></tr>

  <tr><td class="px" style="padding:26px 40px 44px;text-align:center;">{btn(SITE+'/menu?tab=late-night','See the full menu',PINK,'#fff')}</td></tr>

  <!-- $25 band -->
  <tr><td style="padding:0;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:{PINK};">
      <tr><td class="px" style="padding:40px 40px 34px;text-align:center;">
        <p style="margin:0 0 10px;font-family:{Bo};font-size:11px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:#ffd9ee;">Last chance · ends Sunday 4pm</p>
        <h2 class="h2" style="margin:0 0 6px;font-family:{H};font-size:42px;line-height:38px;font-weight:700;text-transform:uppercase;color:#fff;">2 House Margs<br>+ Chips &amp; Dip</h2>
        <p class="big" style="margin:12px 0 10px;font-family:{H};font-size:104px;line-height:88px;font-weight:700;color:{YEL};">$25</p>
        <p style="margin:0 0 24px;font-family:{Bo};font-size:15px;line-height:25px;color:#ffe7f5;">Salsa, guac, or queso. All day, through Sunday.</p>
        <img src="{IMG['margov']}" width="200" alt="House margarita" style="width:200px;max-width:200px;margin:0 auto;border-radius:50%;">
      </td></tr>
    </table>
  </td></tr>

  <!-- brunch -->
  <tr><td style="padding:0;">
    <img src="{IMG['brunch']}" width="600" alt="Churro french toast" style="width:100%;max-width:600px;">
  </td></tr>
  <tr><td class="px" style="padding:34px 40px 44px;text-align:center;background:#12151B;">
    <p style="margin:0 0 10px;font-family:{Bo};font-size:11px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:{YEL};">Sundays · 10am–4pm</p>
    <h2 class="h2" style="margin:0 0 14px;font-family:{H};font-size:42px;line-height:38px;font-weight:700;text-transform:uppercase;color:#fff;">And then, brunch.</h2>
    <p style="margin:0 0 26px;font-family:{Bo};font-size:15px;line-height:26px;color:#9aa4b2;">Churro french toast. Birria. A margarita at 10am, guilt-free.<br>Sundays fill up — get your table locked in.</p>
    {btn(SITE+'/reservations','Reserve a table',BLUE,INK)}
  </td></tr>

  <tr><td class="px" style="padding:40px 40px 36px;text-align:center;background:{INK};">
    <p style="margin:0;font-family:{H};font-size:38px;line-height:36px;font-weight:700;text-transform:uppercase;color:{PINK};">Get a little lost.</p>
  </td></tr>

  {footer('#12151B','#ffffff','#6f7987',IMG['logo_w'],'#2a303a')}

</table></td></tr></table>"""

open("mockup-2-after-dark.html","w").write(page(
 "Uno Más — After Dark",
 "New Late Night Happy Hour, Fri & Sat 8–10pm. Plus $25 margs + chips, ending Sunday.", body, INK))
print("wrote 2")
