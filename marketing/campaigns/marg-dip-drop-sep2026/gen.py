import io
B="https://res.cloudinary.com/drxrfyq9i/image/upload"
WORDN=f"{B}/c_fit,w_1200,f_png/uno-mas/website/logos/um-logo-t-t-blue"

G="e_saturation:18,e_contrast:10,e_brightness:4"
def ph(pid,w,h,g="auto"):
    return f"{B}/{G}/c_fill,g_{g},w_{w},h_{h},f_auto,q_auto/{pid}"
P_OFFER = ph("uno-mas/approved-assets/photos/food/20260814_UM_FOOD_ChipsGuacTrio_v1",1800,860)
P_TRIO  = ph("20260125_UM_FOOD_ChipDipTrioV2_FINAL",1400,820)
P_PATIO = ph("uno-mas/approved-assets/photos/food/20260814_UM_FOOD_ChipsGuacTrio_v4",1200,760)
P_MARG  = ph("20260125_UM_DRINK_Marg_FINAL",900,760)
P_SALSA = ph("uno-mas/approved-assets/photos/food/20260730_UM_FOOD_ChipsSalsa_v2",900,760)

CSS=io.open('style.css',encoding='utf-8').read()

SMS=[("Tue 1 Sep","Announce &mdash; program only, no detail",
      "New Weekly Promo Drop lands tomorrow. Wed-Sun only. You'll want to be here.",75),
     ("Wed 2 Sep","Reveal",
      "This week's drop: 2 house margs + your chips &amp; dip, $25. Wed-Sun. Ask your server.",83),
     ("Sat 5 Sep","Last call",
      "Last call on the $25 drop: 2 house margs + your chips &amp; dip. Ends Sunday.",73)]

DEC=[("Late Night carve-out &mdash; confirm it goes on the piece",
  "<b>Recommend yes, and it is not really optional.</b> Late Night Happy Hour runs Friday and Saturday 8&ndash;10pm with "
  "its own margarita pricing, and the two offers work against each other in that window. Without the line the floor has "
  "no rule and will improvise. It is written into the poster, the tile and the email as drafted."),
 ("Dip pricing &mdash; verify on both printed menus",
  "The Lunch and Dinner PDFs already disagree with each other on the Chip &amp; Dip Trio, so the individual dips are "
  "worth a look before anything goes to print. Nothing on this page quotes a menu price, but the floor still needs to "
  "ring all three correctly."),
 ("Fourth bundle in five weeks &mdash; is that deliberate?",
  "Tests 2, 3 and now 5 are all bundles. The gift card was the one structurally different test, and it is the one you "
  "just told me worked. Not an objection &mdash; but if the Drop becomes &ldquo;there is always a bundle,&rdquo; the "
  "novelty that made it land wears off.")]

TIMELINE=[("Mon 31 Aug","Approve this page. Confirm the Late Night carve-out.","Ramsey"),
 ("Tue 1 Sep","Announce SMS &mdash; program only, no detail. Brief the floor.","Ramsey / Claude"),
 ("Tue 1 Sep","Posters printed and on tables. Website tile pushed, gated Wed&ndash;Sun.","Team / Claude"),
 ("Wed 2 Sep","Reveal SMS and email. Offer goes live.","Claude drafts, Ramsey sends"),
 ("Wed 2 Sep","Meta ads live, if running paid.","Ramsey"),
 ("Sat 5 Sep","Last-call SMS.","Ramsey"),
 ("Sun 6 Sep","Offer ends at close.","&mdash;"),
 ("Mon 7 Sep","Log check average, redemption count and attach rate.","Claude")]

H=[]; A=H.append
A('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">')
A('<meta name="viewport" content="width=device-width,initial-scale=1"><title>Two Margs + A Dip</title>')
A("<style>@import url('https://fonts.googleapis.com/css2?family=Antonio:wght@400;600;700&family=Montserrat:wght@400;600;700;800;900&family=Yellowtail&display=swap');")
A(CSS+'</style></head><body>')
A('<button class="print" onclick="window.print()">Save as PDF</button>')

A(f'<div class="site"><div class="wrap"><img src="{WORDN}" alt="Uno Mas Tacos and Tequila">'
  '<nav><a href="#offer">The offer</a><a href="#how">How it works</a><a href="#words">The words</a>'
  '<a href="#floor">For the floor</a></nav>'
  '</div></div>')

A('<div class="hero"><div class="wrap"><div class="kick">The Weekly Promo Drop</div>'
  '<h1 class="big">Two Margs<br><em>+ A Dip</em></h1>'
  '<div class="price">$25</div>'
  '<div class="sub">Two house margaritas plus your choice<br>of a chips and dip shareable</div>'
  '<div class="dates">Wednesday 2 September &ndash; Sunday 6 September</div>'
  '<div class="askline">Just ask your server.</div></div></div>'
  f'<figure class="shot band"><img src="{P_OFFER}" alt="Two house margaritas with chips and guacamole on a table at Uno Mas"></figure>')

A('<section id="offer"><div class="wrap"><div class="eyebrow">The detail</div>'
  '<h2>What it is, <span>exactly</span></h2>'
  '<p class="lede">Test five in the Weekly Promo Drop. Announced Tuesday with no detail, revealed Wednesday, '
  'runs through Sunday.</p><div class="rule"></div>'
  '<dl class="spec">'
  '<div><dt>Offer</dt><dd><b>Two house margaritas plus your choice of a chips and dip shareable &mdash; $25</b></dd></div>'
  '<div><dt>The shareable</dt><dd><b>Any of them.</b> Chips &amp; salsa, chips &amp; guacamole, or chips &amp; queso blanco '
  '&mdash; whichever the guest wants</dd></div>'
  '<div><dt>Window</dt><dd>Wednesday 2 September &ndash; Sunday 6 September 2026, all day</dd></div>'
  '<div><dt>Exclusion</dt><dd><b>Not valid 8&ndash;10pm Friday and Saturday</b>, during Late Night Happy Hour</dd></div>'
  '<div><dt>Redemption</dt><dd>Ask your server. No code, no app, nothing to show</dd></div>'
  '<div><dt>Limit</dt><dd><b>No limit.</b> Order it as many times as you like, per visit</dd></div>'
  '<div><dt>Drinks</dt><dd><b>House margaritas only.</b> Cadillac and flavored margs are not part of the offer</dd></div>'
  '</dl>'
  f'<figure class="shot inline"><img src="{P_TRIO}" alt="Chips with salsa, guacamole and queso blanco">'
  '<figcaption>Any of the three &mdash; guest&rsquo;s choice</figcaption></figure>'
  '</div></section>')

A('<section id="how"><div class="wrap"><div class="eyebrow">How it works</div>'
  '<h2>Three things <span>to say</span></h2><div class="rule"></div>'
  '<div class="steps">'
  '<div class="step"><div class="n">1</div><h3>Just ask</h3><p>No code word this week, no app, nothing to show. '
  'A guest asks and the server rings it.</p></div>'
  '<div class="step"><div class="n">2</div><h3>Pick a shareable</h3><p>Chips and salsa, chips and guacamole, or chips '
  'and queso blanco. No wrong answer, nothing to explain.</p></div>'
  '<div class="step"><div class="n">3</div><h3>Again if you like</h3><p>No limit. Two more margs and another dip '
  'is another $25 &mdash; this is an upsell, not a coupon.</p></div>'
  '</div>'
  f'<div class="duo"><figure class="shot"><img src="{P_MARG}" alt="House margarita"></figure>'
  f'<figure class="shot"><img src="{P_SALSA}" alt="Basket of chips with salsa"></figure></div>'
  '</div></section>')

A('<section id="words"><div class="wrap"><div class="eyebrow">The words</div>'
  '<h2>Every message, <span>written</span></h2>'
  '<p class="lede">Toast prepends the restaurant name and appends the opt-out, so neither appears in the body. '
  'All three texts avoid the accented &aacute; in &ldquo;M&aacute;s&rdquo; and any curly quote or dash &mdash; those force a '
  'different encoding that cuts a message from 160 characters to 70 and roughly doubles what a send costs.</p>'
  '<div class="rule"></div>'
  '<div class="copygrid">'
  +''.join(f'<div class="cc"><div class="when">{d}</div><div class="role">{r}</div>'
           f'<div class="msg">{m}</div><div class="tech">{c} characters &middot; <b>single message</b></div></div>'
           for d,r,m,c in SMS)
  +'</div>'
  '<h3 class="minor">Email subject lines</h3>'
  '<ul class="plain">'
  '<li>Two margs and a dip. $25.</li>'
  '<li>This week: two margs and a dip</li>'
  '<li>Start with the good stuff</li>'
  '<li>The drop is live. Two margs + a dip.</li>'
  '</ul>'
  '<div class="callout"><b>Preheader:</b> &ldquo;Wednesday through Sunday. Ask your server &mdash; no code needed.&rdquo;</div>'
  '<h3 class="minor">Email body</h3>'
  '<div class="callout">Two house margaritas plus your choice of a chips and dip shareable &mdash; salsa, guacamole or queso blanco. '
  '<b>$25.</b><br><br>No code, no app, nothing to show us. Just ask your server &mdash; and there is no limit, so bring '
  'people.<br><br><span style="color:var(--mut);font-size:14px">Footer: House margaritas only. No limit per visit. '
  'Not valid 8&ndash;10pm Friday &amp; Saturday during Late Night Happy Hour.</span></div>'
  '<h3 class="minor">Meta ads</h3>'
  '<ul class="plain">'
  '<li>Two house margs plus your choice of a chips and dip shareable. $25, Wednesday through Sunday. Monroe Street, Spokane.'
  '<span>Primary text A</span></li>'
  '<li>The kind of order that turns into staying longer than you planned. Two margs, a dip, $25. This week only.'
  '<span>Primary text B</span></li>'
  '<li>Two Margs + A Dip &mdash; $25<span>Headline</span></li>'
  '<li>Wed&ndash;Sun. Ask your server.<span>Description</span></li>'
  '<li>Learn More<span>Call to action &mdash; not Order Now, this is dine-in</span></li>'
  '</ul></div></section>')

A('<section id="floor"><div class="wrap"><div class="eyebrow">For the floor</div>'
  '<h2>Brief this, <span>don&rsquo;t just post it</span></h2><div class="rule"></div>'
  '<ul class="rules">'
  '<li><b>Two house margs plus one chips and dip shareable &mdash; $25.</b></li>'
  '<li><b>Any of the three dips.</b> Salsa, guacamole or queso blanco &mdash; guest&rsquo;s choice. No upcharge, '
  'no steering.</li>'
  '<li><b>Not available 8&ndash;10pm Friday and Saturday.</b> Late Night Happy Hour has its own margarita pricing. '
  'If someone asks in that window, point them at Late Night instead.</li>'
  '<li><b>House margaritas only.</b> Cadillac and flavored margs are not part of the offer.</li>'
  '<li><b>No limit.</b> A table can run it as many times as they want. Two more margs and another dip is another $25 '
  '&mdash; say it.</li>'
  '<li><b>No code word this week.</b> They just ask.</li>'
  '</ul>'
  f'<figure class="shot inline"><img src="{P_PATIO}" alt="Chips and dips with two margaritas on a patio table"></figure>'
  '</div></section>')

A('<footer class="pg"><div class="wrap"><span class="sc">Get a little lost.</span>'
  'Uno M&aacute;s Tacos &amp; Tequila &middot; 2020 N Monroe St, Suite C, Spokane<br>'
  'Internal review page &mdash; nothing on it is live or printed. Drafted 31 August 2026.</div></footer>')
A('</body></html>')
io.open('promo-overview.html','w',encoding='utf-8').write("\n".join(H))
print("written", sum(len(x) for x in H))
