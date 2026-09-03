from _shared import *
CREAM="#FFFBEF"
btn = lambda href,label,bg,fg: f"""<table role="presentation" cellpadding="0" cellspacing="0" style="margin:0 auto;"><tr><td style="background:{bg};"><a href="{href}" style="display:inline-block;padding:15px 32px;font-family:{H};font-size:19px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:{fg};">{label}</a></td></tr></table>"""
dots = f'<div style="height:6px;background:repeating-linear-gradient(90deg,{PINK} 0 6px,transparent 6px 14px);"></div>'

body = f"""
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#EFE9D8;"><tr><td align="center" style="padding:0 0 40px;">
<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" style="width:600px;max-width:600px;background:{CREAM};border-left:8px solid {NAVY};border-right:8px solid {NAVY};">

  <tr><td style="background:{NAVY};padding:24px 32px;text-align:center;">
    <img src="{IMG['logo_w']}" width="180" alt="Uno Más" style="width:180px;margin:0 auto;">
  </td></tr>
  <tr><td>{dots}</td></tr>

  <!-- BIG $25 poster -->
  <tr><td class="px" style="padding:38px 40px 0;text-align:center;">
    <table role="presentation" cellpadding="0" cellspacing="0" style="margin:0 auto 22px;"><tr><td style="background:{PINK};padding:9px 26px;">
      <span style="font-family:{Bo};font-size:12px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:#fff;">Limited time promo</span>
    </td></tr></table>
    <h1 class="h1" style="margin:0 0 4px;font-family:{H};font-size:60px;line-height:52px;font-weight:700;text-transform:uppercase;color:{NAVY};">2 House Margs</h1>
    <p style="margin:6px 0 4px;font-family:{H};font-size:34px;line-height:32px;color:{PINK};font-weight:700;">+</p>
    <h1 class="h1" style="margin:0 0 22px;font-family:{H};font-size:60px;line-height:52px;font-weight:700;text-transform:uppercase;color:{PINK};">Chips &amp; Dip</h1>
    <table role="presentation" cellpadding="0" cellspacing="0" style="margin:0 auto;"><tr><td style="background:{YEL};padding:10px 42px;">
      <span class="big" style="font-family:{H};font-size:118px;line-height:98px;font-weight:700;color:{NAVY};">$25</span>
    </td></tr></table>
  </td></tr>

  <tr><td class="px" style="padding:26px 40px 0;">
    <img src="{IMG['flight']}" width="504" alt="Margaritas" style="width:100%;max-width:504px;">
  </td></tr>

  <tr><td class="px" style="padding:24px 40px 0;text-align:center;">
    <table role="presentation" cellpadding="0" cellspacing="0" style="margin:0 auto 16px;"><tr><td style="background:{BLUE};padding:6px 18px;">
      <span style="font-family:{Bo};font-size:11px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#fff;">Choose</span>
    </td><td style="padding:0 0 0 12px;">
      <span style="font-family:{Bo};font-size:17px;font-style:italic;color:{NAVY};">Your chips and dip.</span>
    </td></tr></table>
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
      <td class="stack" width="33.3%" style="text-align:center;padding:6px;">
        <div style="background:{PINK};padding:8px 0;"><span style="font-family:{H};font-size:20px;font-weight:700;letter-spacing:.06em;color:#fff;">SALSA</span></div>
      </td>
      <td class="stack" width="33.3%" style="text-align:center;padding:6px;">
        <div style="background:{PINK};padding:8px 0;"><span style="font-family:{H};font-size:20px;font-weight:700;letter-spacing:.06em;color:#fff;">GUAC</span></div>
      </td>
      <td class="stack" width="33.3%" style="text-align:center;padding:6px;">
        <div style="background:{PINK};padding:8px 0;"><span style="font-family:{H};font-size:20px;font-weight:700;letter-spacing:.06em;color:#fff;">QUESO</span></div>
      </td>
    </tr></table>
  </td></tr>

  <tr><td class="px" style="padding:22px 40px 34px;text-align:center;">
    <div style="background:{NAVY};padding:12px;">
      <span style="font-family:{H};font-size:24px;font-weight:700;letter-spacing:.1em;color:{YEL};">⚡ ALL DAY — ENDS SUNDAY ⚡</span>
    </div>
  </td></tr>

  <tr><td>{dots}</td></tr>

  <!-- late night -->
  <tr><td class="px" style="padding:36px 40px 0;text-align:center;background:{NAVY};">
    <p style="margin:0 0 10px;font-family:{Bo};font-size:11px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:{BLUE};">Now running · Fri &amp; Sat · 8–10pm</p>
    <h2 class="h2" style="margin:0 0 18px;font-family:{H};font-size:46px;line-height:42px;font-weight:700;text-transform:uppercase;color:#fff;">Late Night<br>Happy Hour</h2>
    <table role="presentation" cellpadding="0" cellspacing="0" style="margin:0 auto 18px;"><tr><td style="background:{YEL};padding:8px 26px;">
      <span style="font-family:{H};font-size:30px;font-weight:700;color:{NAVY};">ANY TWO STREET TACOS — $10</span>
    </td></tr></table>
    <p style="margin:0 0 20px;font-family:{Bo};font-size:13px;line-height:24px;color:#a9c3dd;">Carne Asada · Al Pastor Chicken · Carnitas<br>Barbacoa · Batata · Hongos</p>
    <p style="margin:0 0 26px;font-family:{H};font-size:26px;line-height:34px;color:#fff;font-weight:600;letter-spacing:.04em;">
      MARGS <span style="color:{PINK};">$6</span> &nbsp; PINTS <span style="color:{PINK};">$5</span><br>
      SHOTS <span style="color:{PINK};">$4</span> &nbsp; PITCHERS <span style="color:{PINK};">$30</span>
    </p>
  </td></tr>
  <tr><td class="px" style="padding:0 40px 36px;text-align:center;background:{NAVY};">{btn(SITE+'/menu?tab=late-night','See the menu',PINK,'#fff')}</td></tr>

  <tr><td>{dots}</td></tr>

  <!-- brunch -->
  <tr><td class="px" style="padding:36px 40px 0;text-align:center;">
    <p style="margin:0 0 10px;font-family:{Bo};font-size:11px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:{BLUE};">Sundays · 10am–4pm</p>
    <h2 class="h2" style="margin:0 0 16px;font-family:{H};font-size:46px;line-height:42px;font-weight:700;text-transform:uppercase;color:{NAVY};">Sunday Brunch</h2>
    <img src="{IMG['brunchsq']}" width="240" alt="Churro french toast" style="width:240px;max-width:240px;margin:0 auto 20px;">
    <p style="margin:0 0 24px;font-family:{Bo};font-size:15px;line-height:25px;color:#54514a;">Churro french toast, birria, and a marg before noon.<br>Book it — Sundays go quick.</p>
    {btn(SITE+'/reservations','Reserve a table',NAVY,'#fff')}
  </td></tr>

  <tr><td class="px" style="padding:40px 40px 38px;text-align:center;">
    <p style="margin:0;font-family:{H};font-size:40px;line-height:38px;font-weight:700;text-transform:uppercase;color:{PINK};">Get a little lost.</p>
  </td></tr>

  {footer(NAVY,'#ffffff','#93a7bd',IMG['logo_w'],'#38536e')}

</table></td></tr></table>"""

open("mockup-3-table-tent.html","w").write(page(
 "Uno Más — $25 Margs & Chips",
 "2 house margs + chips & dip, $25 — ends Sunday. Plus Late Night Happy Hour and brunch.", body, "#EFE9D8"))
print("wrote 3")
