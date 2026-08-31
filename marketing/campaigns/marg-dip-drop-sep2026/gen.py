import io
B="https://res.cloudinary.com/drxrfyq9i/image/upload"
WORDN=f"{B}/c_fit,w_1200,f_png/uno-mas/website/logos/um-logo-t-t-blue"
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
  '<a href="#floor">For the floor</a><a href="#week">Run of week</a><a href="#decide">Before we build</a></nav>'
  '</div></div>')

A('<div class="hero"><div class="wrap"><div class="kick">The Weekly Promo Drop</div>'
  '<h1 class="big">Two Margs<br><em>+ A Dip</em></h1>'
  '<div class="price">$25</div>'
  '<div class="sub">Two house margaritas<br>+ your choice of chips &amp; dip</div>'
  '<div class="dates">Wednesday 2 September &ndash; Sunday 6 September</div>'
  '<div class="askline">Just ask your server.</div></div></div>')

A('<section id="offer"><div class="wrap"><div class="eyebrow">The detail</div>'
  '<h2>What it is, <span>exactly</span></h2>'
  '<p class="lede">Test five in the Weekly Promo Drop. Announced Tuesday with no detail, revealed Wednesday, '
  'runs through Sunday.</p><div class="rule"></div>'
  '<dl class="spec">'
  '<div><dt>Offer</dt><dd><b>Two house margaritas + your choice of chips &amp; dip &mdash; $25</b></dd></div>'
  '<div><dt>Dips</dt><dd><b>Any of the three.</b> Chips &amp; salsa, chips &amp; guacamole, or chips &amp; queso blanco &mdash; '
  'whichever the guest wants</dd></div>'
  '<div><dt>Window</dt><dd>Wednesday 2 September &ndash; Sunday 6 September 2026, all day</dd></div>'
  '<div><dt>Exclusion</dt><dd><b>Not valid 8&ndash;10pm Friday and Saturday</b>, during Late Night Happy Hour</dd></div>'
  '<div><dt>Redemption</dt><dd>Ask your server. No code, no app, nothing to show</dd></div>'
  '<div><dt>Limit</dt><dd><b>No limit.</b> Order it as many times as you like, per visit</dd></div>'
  '<div><dt>Drinks</dt><dd><b>House margaritas only.</b> Cadillac and flavored margs are not part of the offer</dd></div>'
  '</dl></div></section>')

A('<section id="how"><div class="wrap"><div class="eyebrow">How it works</div>'
  '<h2>Three things <span>to say</span></h2><div class="rule"></div>'
  '<div class="steps">'
  '<div class="step"><div class="n">1</div><h3>Just ask</h3><p>No code word this week, no app, nothing to show. '
  'A guest asks and the server rings it.</p></div>'
  '<div class="step"><div class="n">2</div><h3>Pick a dip</h3><p>Salsa, guacamole or queso blanco. Whichever they '
  'want &mdash; no wrong answer, nothing to explain.</p></div>'
  '<div class="step"><div class="n">3</div><h3>Again if you like</h3><p>No limit. Two more margs and another dip '
  'is another $25 &mdash; this is an upsell, not a coupon.</p></div>'
  '</div></div></section>')

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
  '<div class="callout">Two house margaritas and your pick of chips &amp; dip &mdash; salsa, guacamole or queso blanco. '
  '<b>$25.</b><br><br>No code, no app, nothing to show us. Just ask your server &mdash; and there is no limit, so bring '
  'people.<br><br><span style="color:var(--mut);font-size:14px">Footer: House margaritas only. No limit per visit. '
  'Not valid 8&ndash;10pm Friday &amp; Saturday during Late Night Happy Hour.</span></div>'
  '<h3 class="minor">Meta ads</h3>'
  '<ul class="plain">'
  '<li>Two house margs and your pick of chips &amp; dip. $25, Wednesday through Sunday. Monroe Street, Spokane.'
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
  '<li><b>Two house margs plus one chips &amp; dip &mdash; $25.</b></li>'
  '<li><b>Any of the three dips.</b> Salsa, guacamole or queso blanco &mdash; guest&rsquo;s choice. No upcharge, '
  'no steering.</li>'
  '<li><b>Not available 8&ndash;10pm Friday and Saturday.</b> Late Night Happy Hour has its own margarita pricing. '
  'If someone asks in that window, point them at Late Night instead.</li>'
  '<li><b>House margaritas only.</b> Cadillac and flavored margs are not part of the offer.</li>'
  '<li><b>No limit.</b> A table can run it as many times as they want. Two more margs and another dip is another $25 '
  '&mdash; say it.</li>'
  '<li><b>No code word this week.</b> They just ask.</li>'
  '</ul></div></section>')

A('<section id="week"><div class="wrap"><div class="eyebrow">Logistics</div>'
  '<h2>Run of <span>the week</span></h2><div class="rule"></div>'
  '<table class="tl"><thead><tr><th>When</th><th>What</th><th>Who</th></tr></thead><tbody>'
  +''.join(f'<tr><td>{w}</td><td>{x}</td><td>{y}</td></tr>' for w,x,y in TIMELINE)
  +'</tbody></table></div></section>')

A('<section id="decide"><div class="wrap"><div class="eyebrow">Before we build</div>'
  '<h2>Three things <span>we need settled</span></h2>'
  '<p class="lede">Nothing here is live and nothing is printed. The first one changes what the floor is told.</p>'
  '<div class="rule"></div>'
  +''.join(f'<div class="dec"><div class="q">{q}</div><div class="r">{r}</div></div>' for q,r in DEC)
  +'</div></section>')

A('<section><div class="wrap"><div class="eyebrow">Afterwards</div>'
  '<h2>What we <span>learn from it</span></h2>'
  '<p class="lede">Four tests have run and none has a number attached. That is the real gap, not the creative.</p>'
  '<div class="rule"></div>'
  '<ul class="plain" style="margin-top:28px">'
  '<li>Average check Wednesday&ndash;Sunday against the same days the week before'
  '<span>The number that says whether it worked</span></li>'
  '<li>Redemption count<span>How many actually ordered it</span></li>'
  '<li>Attach rate<span>Did they add the dip, or swap it for something they would have ordered anyway</span></li>'
  '<li>Which dip they picked<span>Now that all three are in, this tells us which one to lead with next time</span></li>'
  '</ul>'
  '<div class="callout">The Toast dashboard is the tool for this, but <b>its API credentials currently fail '
  'authentication</b> &mdash; so this will be a manual pull unless that gets fixed first. Worth an hour before '
  'Wednesday.</div></div></section>')

A('<footer class="pg"><div class="wrap"><span class="sc">Get a little lost.</span>'
  'Uno M&aacute;s Tacos &amp; Tequila &middot; 2020 N Monroe St, Suite C, Spokane<br>'
  'Internal review page &mdash; nothing on it is live or printed. Drafted 31 August 2026.</div></footer>')
A('</body></html>')
io.open('promo-overview.html','w',encoding='utf-8').write("\n".join(H))
print("written", sum(len(x) for x in H))
