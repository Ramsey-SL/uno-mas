import io
B="https://res.cloudinary.com/drxrfyq9i/image/upload"
WORDN=f"{B}/c_fit,w_1200,f_png/uno-mas/website/logos/um-logo-t-t-blue"
G="e_saturation:18,e_contrast:10,e_brightness:4"
def ph(pid,w,h,g="auto"): return f"{B}/{G}/c_fill,g_{g},w_{w},h_{h},f_auto,q_auto/{pid}"
F="uno-mas/approved-assets/photos/food/"
T1=ph(F+"20260814_UM_FOOD_ChipsGuacTrio_v1",620,620)
T2=ph("20260125_UM_FOOD_ChipDipTrioV2_FINAL",620,620)
T3=ph("20260125_UM_DRINK_Marg_FINAL",620,620)
T4=ph(F+"20260814_UM_FOOD_ChipsGuacTrio_v4",620,620)
P_TRIO =ph("20260125_UM_FOOD_ChipDipTrioV2_FINAL",1400,780)
P_MARG =ph("20260125_UM_DRINK_Marg_FINAL",900,760)
P_SALSA=ph(F+"20260730_UM_FOOD_ChipsSalsa_v2",900,760)
P_PATIO=ph(F+"20260814_UM_FOOD_ChipsGuacTrio_v4",1200,700)
CSS=io.open('style.css',encoding='utf-8').read()

H=[]; A=H.append
A('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">')
A('<meta name="viewport" content="width=device-width,initial-scale=1"><title>Two Margs + A Chips &amp; Dip Shareable</title>')
A("<style>@import url('https://fonts.googleapis.com/css2?family=Antonio:wght@400;600;700&family=Montserrat:wght@400;600;700;800;900&family=Yellowtail&display=swap');")
A(CSS+'</style></head><body>')
A('<button class="print" onclick="window.print()">Save as PDF</button>')

A(f'<div class="site"><div class="wrap"><img src="{WORDN}" alt="Uno Mas Tacos and Tequila">'
  '<nav><a href="#offer">The offer</a><a href="#how">How it works</a><a href="#floor">For the floor</a>'
  '<a href="#week">The week</a></nav></div></div>')

A('<div class="hero"><div class="wrap"><div class="kick">The Weekly Promo Drop</div>'
  '<h1 class="big">Two Margs +<br><em>A Chips &amp; Dip Shareable</em></h1>'
  '<div class="price">$25</div>'
  '<div class="sub">Two house margaritas plus your choice<br>of a chips and dip shareable.</div>'
  '<div class="dates">Drops Wednesday &middot; runs through Sunday</div>'
  '<div class="askline">Just ask your server.</div></div></div>')

A('<div class="tilerow"><div class="wrap"><div class="tiles">'
  f'<figure class="shot"><img src="{T1}" alt="Two margaritas with chips and guacamole"></figure>'
  f'<figure class="shot"><img src="{T2}" alt="Chips with salsa, guacamole and queso blanco"></figure>'
  f'<figure class="shot"><img src="{T3}" alt="House margarita"></figure>'
  f'<figure class="shot"><img src="{T4}" alt="Chips and dips with margaritas on a patio table"></figure>'
  '</div></div></div>')

A('<section id="offer"><div class="wrap"><div class="eyebrow">The detail</div>'
  '<h2>What it is, <span>exactly</span></h2>'
  '<p class="lede">Drops Wednesday.</p><div class="rule"></div>'
  '<dl class="spec">'
  '<div><dt>Offer</dt><dd><b>Two house margaritas plus your choice of a chips and dip shareable &mdash; $25</b></dd></div>'
  '<div><dt>The shareable</dt><dd><b>Any of them.</b> Chips &amp; salsa, chips &amp; guacamole, or chips &amp; queso blanco '
  '&mdash; whichever the guest wants</dd></div>'
  '<div><dt>Window</dt><dd>Wednesday 2 September &ndash; Sunday 6 September, all day</dd></div>'
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
  '<div class="step"><div class="n">3</div><h3>Again if you like</h3><p>No limit. Two more margs and another shareable '
  'is another $25 &mdash; this is an upsell, not a coupon.</p></div>'
  '</div>'
  f'<div class="duo"><figure class="shot"><img src="{P_MARG}" alt="House margarita"></figure>'
  f'<figure class="shot"><img src="{P_SALSA}" alt="Basket of chips with salsa"></figure></div>'
  '</div></section>')

A('<section id="floor"><div class="wrap"><div class="eyebrow">For the floor</div>'
  '<h2>Brief this, <span>don&rsquo;t just post it</span></h2><div class="rule"></div>'
  '<ul class="rules">'
  '<li><b>Two house margs plus one chips and dip shareable &mdash; $25.</b></li>'
  '<li><b>Any of the three shareables.</b> Salsa, guacamole or queso blanco &mdash; guest&rsquo;s choice. No upcharge, '
  'no steering.</li>'
  '<li><b>Not available 8&ndash;10pm Friday and Saturday.</b> Late Night Happy Hour has its own margarita pricing. '
  'If someone asks in that window, point them at Late Night instead.</li>'
  '<li><b>House margaritas only.</b> Cadillac and flavored margs are not part of the offer.</li>'
  '<li><b>No limit.</b> A table can run it as many times as they want. Two more margs and another shareable is another '
  '$25 &mdash; say it.</li>'
  '<li><b>No code word this week.</b> They just ask.</li>'
  '</ul>'
  f'<figure class="shot inline"><img src="{P_PATIO}" alt="Chips and dips with two margaritas on a patio table"></figure>'
  '</div></section>')

# ── the week: messaging framework ──
A('<section id="week"><div class="wrap"><div class="eyebrow">Messaging framework</div>'
  '<h2>Four things to say, <span>three sends</span></h2>'
  '<p class="lede">Two texts and one email this week. That is fewer sends than things worth saying, so each one has '
  'to carry more than the drop. The email is the only surface wide enough to hold all four.</p><div class="rule"></div>'
  '<div class="needs">'
  '<div class="need"><div class="r">1</div><h4>The drop</h4><p>New, expires Sunday. Only thing here with a deadline.</p></div>'
  '<div class="need"><div class="r">2</div><h4>Late Night Happy Hour</h4><p>Fri &amp; Sat, 8&ndash;10pm. Still new enough that people do not know it exists.</p></div>'
  '<div class="need"><div class="r">3</div><h4>Wed &amp; Thu specials</h4><p>Beer &amp; Bites and Big F&rsquo;N Thursday. Standing, and the soft days.</p></div>'
  '<div class="need"><div class="r">4</div><h4>Brunch</h4><p>Every Sunday, 10&ndash;4. Ongoing push, no deadline.</p></div>'
  '</div>'

  '<div class="send"><div class="hd"><span class="ch">SMS one</span><span class="dt">Wed 2 Sep</span>'
  '<span class="carries">Carries: the drop + Wednesday</span></div>'
  '<div class="msg">The drop is live: 2 house margs + a chips and dip shareable, $25. Also every Wednesday, $5 pints. '
  'Runs Wed-Sun.</div>'
  '<div class="tech">111 characters &middot; <b>single message</b> &middot; Toast adds the name and the opt-out</div></div>'

  '<div class="send"><div class="hd"><span class="ch">Email</span><span class="dt">Wed 2 Sep</span>'
  '<span class="carries">Carries: all four</span></div>'
  '<ul class="em">'
  '<li><b>Hero &mdash; the drop.</b> Two house margs plus your choice of a chips and dip shareable, $25. Wednesday '
  'through Sunday. Ask your server.<span>Photo: the two-margs-and-guac shot</span></li>'
  '<li><b>Then &mdash; Late Night Happy Hour.</b> Friday and Saturday, 8&ndash;10pm. The one people still do not know '
  'about, so it gets real space rather than a footnote.<span>This is the block to watch clicks on</span></li>'
  '<li><b>Then &mdash; this week on the calendar.</b> Beer &amp; Bites Wednesday and Big F&rsquo;N Thursday, side by '
  'side.<span>Two soft days, one module</span></li>'
  '<li><b>Close &mdash; brunch.</b> Every Sunday, 10 to 4. Sits last because it has no deadline and it is the natural '
  'next visit after a Saturday night.<span>Photo: horchata french toast</span></li>'
  '</ul></div>'

  '<div class="send"><div class="hd"><span class="ch">SMS two</span><span class="dt">Sat 5 Sep</span>'
  '<span class="carries">Carries: Late Night + brunch + last call</span></div>'
  '<div class="msg">Late night tonight, 8-10pm. Brunch tomorrow, 10-4. And the $25 marg + shareable drop ends Sunday.</div>'
  '<div class="tech">97 characters &middot; <b>single message</b> &middot; three things, one send</div></div>'

  '<h3 class="minor">Two other ways to split it</h3>'
  '<p class="lede">Same three sends, different allocation. Worth a look before we lock it.</p>'
  '<div class="alts">'
  '<div class="alt"><div class="t">Put SMS two on Friday</div>'
  '<p>&ldquo;Late Night Happy Hour tonight and tomorrow, 8&ndash;10pm. The $25 marg + shareable drop runs till Sunday.&rdquo; '
  'Catches Late Night before the first of its two nights instead of the second.</p>'
  '<div class="give">Gives up: brunch in SMS, and the Sunday last call.</div></div>'
  '<div class="alt"><div class="t">Put SMS two on Sunday</div>'
  '<p>&ldquo;Brunch till 4 today, and it is the last day for the $25 marg + shareable drop.&rdquo; Two deadlines in one '
  'text, sent the morning they both matter.</p>'
  '<div class="give">Gives up: Late Night entirely outside the email.</div></div>'
  '</div>'
  '<div class="callout"><b>What none of the three solves:</b> Big F&rsquo;N Thursday only ever appears in the email. '
  'With two texts there is no way to give Thursday its own moment and still cover the drop, Late Night and brunch. '
  'If Thursday matters more than brunch this week, say so and I will swap them.</div>'
  '</div></section>')

A('<footer class="pg"><div class="wrap"><span class="sc">Get a little lost.</span>'
  'Uno M&aacute;s Tacos &amp; Tequila &middot; 2020 N Monroe St, Suite C, Spokane<br>'
  'Internal review page &mdash; nothing on it is live or printed. Drafted 1 September 2026.</div></footer>')
A('</body></html>')
io.open('promo-overview.html','w',encoding='utf-8').write("\n".join(H))
print("written", sum(len(x) for x in H))
