B = "https://res.cloudinary.com/drxrfyq9i/image/upload"
IMG = {
 "marg":   f"{B}/f_auto,q_auto:best,w_1200,h_900,c_fill,g_auto,e_vibrance:30,e_saturation:12/20260623_UM_COCKTAIL_MargaritaOnBar01",
 "margov": f"{B}/f_auto,q_auto:best,w_1000,h_1000,c_fill,g_auto,e_vibrance:30/20260623_UM_COCKTAIL_MargaritaOverhead02",
 "flight": f"{B}/f_auto,q_auto:best,w_1200,h_800,c_fill,g_auto,e_vibrance:25/20260619_UM_DRINK_MargaritaFlight_v1",
 "tacos2": f"{B}/f_auto,q_auto:best,w_1200,h_800,c_fill,g_auto,e_vibrance:30/20260623_UM_FOOD_TwoStreetTacosTray",
 "flat":   f"{B}/f_auto,q_auto:best,w_1200,h_900,c_fill,g_auto,e_vibrance:30/20260623_UM_FOOD_StreetTacosWithMargarita01",
 "plate":  f"{B}/f_auto,q_auto:best,w_1000,h_1000,c_fill,g_auto,e_vibrance:30/20260623_UM_FOOD_StreetTacosPlate",
 "brunch": f"{B}/f_auto,q_auto:best,w_1200,h_900,c_fill,g_auto,e_vibrance:20/uno-mas/approved-assets/photos/brunch/20260724_UM_BRUNCH_ChurroFrenchToast_v4",
 "brunchsq": f"{B}/f_auto,q_auto:best,w_1000,h_1000,c_fill,g_auto,e_vibrance:20/uno-mas/approved-assets/photos/brunch/20260724_UM_BRUNCH_ChurroFrenchToast_v4",
 "logo_w": f"{B}/f_auto,q_auto,w_700/uno-mas/website/logos/um-t-t-nooutline-white-asset-2",
 "logo_n": f"{B}/f_auto,q_auto,w_700/uno-mas/website/logos/um-t-t-nooutline-navy-asset-3",
 "logo_p": f"{B}/f_auto,q_auto,w_700/uno-mas/website/logos/um-logo-t-t-pink",
}
PINK="#E22690"; BLUE="#18BCDC"; NAVY="#003366"; YEL="#FFEC00"
SITE="https://unomastacoshop.com"
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
 '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=Antonio:wght@400;600;700&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">')
H = "'Antonio', 'Arial Narrow', Arial, sans-serif"
Bo = "'Montserrat', 'Helvetica Neue', Arial, sans-serif"

def footer(bg, fg, muted, logo, rule):
    return f"""
<tr><td style="background:{bg};padding:36px 32px;text-align:center;">
  <img src="{logo}" width="150" alt="Uno Más Tacos &amp; Tequila" style="width:150px;max-width:150px;display:block;margin:0 auto 20px;">
  <p style="margin:0 0 6px;font-family:{Bo};font-size:13px;line-height:20px;color:{fg};font-weight:600;">2020 N Monroe St, Suite C · Spokane, WA 99205</p>
  <p style="margin:0 0 16px;font-family:{Bo};font-size:13px;line-height:20px;color:{muted};">
    <a href="tel:+15099607989" style="color:{muted};text-decoration:none;">(509) 960-7989</a> &nbsp;·&nbsp;
    <a href="mailto:tacos@unomastacoshop.com" style="color:{muted};text-decoration:none;">tacos@unomastacoshop.com</a>
  </p>
  <p style="margin:0 0 16px;font-family:{Bo};font-size:12px;line-height:19px;color:{muted};">
    Tue–Thu 11am–9pm · Fri–Sat 11am–10pm · Sun 10am–4pm · Closed Mondays
  </p>
  <p style="margin:0 0 20px;font-family:{Bo};font-size:13px;font-weight:600;">
    <a href="https://instagram.com/unomastacoshop" style="color:{fg};text-decoration:none;">Instagram</a>
    <span style="color:{rule};">&nbsp;·&nbsp;</span>
    <a href="https://www.tiktok.com/@unomastacosandtequila" style="color:{fg};text-decoration:none;">TikTok</a>
    <span style="color:{rule};">&nbsp;·&nbsp;</span>
    <a href="{SITE}" style="color:{fg};text-decoration:none;">unomastacoshop.com</a>
  </p>
  <p style="margin:0;font-family:{Bo};font-size:11px;line-height:18px;color:{muted};">
    You're getting this because you're on the list at Uno Más.<br>
    <a href="%unsubscribe%" style="color:{muted};text-decoration:underline;">Unsubscribe</a>
  </p>
</td></tr>"""

def page(title, preheader, body, bg):
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>{FONTS}
<style>
  body{{margin:0;padding:0;background:{bg};-webkit-font-smoothing:antialiased;}}
  img{{border:0;outline:none;text-decoration:none;display:block;}}
  table{{border-collapse:collapse;}}
  a{{text-decoration:none;}}
  @media only screen and (max-width:620px){{
    .wrap{{width:100% !important;}}
    .px{{padding-left:22px !important;padding-right:22px !important;}}
    .stack{{display:block !important;width:100% !important;}}
    .h1{{font-size:44px !important;line-height:44px !important;}}
    .h2{{font-size:32px !important;line-height:34px !important;}}
    .big{{font-size:80px !important;line-height:76px !important;}}
  }}
</style></head>
<body style="margin:0;padding:0;background:{bg};">
<div style="display:none;max-height:0;overflow:hidden;opacity:0;font-size:1px;line-height:1px;color:{bg};">{preheader}</div>
{body}
</body></html>"""
