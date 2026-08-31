import io, random
random.seed(41)
B="https://res.cloudinary.com/drxrfyq9i/image/upload"
SRC="uno-mas/approved-assets/photos/promo/20260814_UM_PROMO_WeekendSpecial_Portrait"
MARGS=f"{B}/c_crop,x_105,y_1880,w_1700,h_1270/c_fit,w_1400,f_png/{SRC}"
QUESO=f"{B}/c_crop,x_2180,y_3120,w_720,h_540/c_fit,w_700,f_png/{SRC}"
GUAC =f"{B}/c_crop,x_1640,y_3140,w_700,h_520/c_fit,w_700,f_png/{SRC}"
WORDW=f"{B}/c_fit,w_1400,f_png/uno-mas/website/logos/um-t-t-nooutline-white-asset-2"

def rough(seed,jl=2.0,jr=2.0,jb=1.5,steps=24):
    r=random.Random(seed); p=[(0,0)]
    for i in range(1,steps): p.append((i*100/steps, r.uniform(0,.8)))
    p.append((100,0))
    for i in range(1,steps): p.append((100-r.uniform(0,jr), i*100/steps))
    p.append((100,100))
    for i in range(1,steps): p.append((100-i*100/steps, 100-r.uniform(0,jb)))
    p.append((0,100))
    for i in range(1,steps): p.append((r.uniform(0,jl), 100-i*100/steps))
    return "polygon("+",".join(f"{x:.2f}% {y:.2f}%" for x,y in p)+")"
def brushd(seed):
    r=random.Random(seed); n=13
    p=[(i*100/n, r.uniform(0,4.2)) for i in range(n+1)]
    p+=[(100-r.uniform(0,3.2), i*100/n) for i in range(1,n)]
    p+=[(100-i*100/n, 100-r.uniform(0,4.2)) for i in range(n+1)]
    p+=[(r.uniform(0,3.2), 100-i*100/n) for i in range(1,n)]
    return "M"+" L".join(f"{x:.1f},{y:.1f}" for x,y in p)+" Z"
TEAR=("polygon(0 0,100% 0,100% calc(100% - 14px),96.5% 100%,93% calc(100% - 11px),89% 100%,85.5% calc(100% - 13px),"
"82% 100%,78% calc(100% - 9px),74.5% 100%,71% calc(100% - 14px),67% 100%,63.5% calc(100% - 10px),60% 100%,"
"56% calc(100% - 13px),52.5% 100%,49% calc(100% - 8px),45% 100%,41.5% calc(100% - 14px),38% 100%,"
"34% calc(100% - 10px),30.5% 100%,27% calc(100% - 12px),23% 100%,19.5% calc(100% - 8px),16% 100%,"
"12% calc(100% - 14px),8.5% 100%,5% calc(100% - 10px),0 100%)")
EDGE=rough(5); BR1=brushd(11)
def BRP(c): return f'<svg class="brst {c}" viewBox="0 0 100 100" aria-hidden="true"><path d="M50,2L57,24L72,10L68,32L90,22L78,40L100,44L78,52L92,68L70,62L74,86L56,72L52,96L44,72L28,88L30,62L8,70L22,52L0,44L22,38L8,20L30,32L28,8L44,24Z" fill="#DC1548"/></svg>'
def BRB(c): return (f'<svg class="brst {c}" viewBox="0 0 100 100" aria-hidden="true">'
 '<path d="M50,0L58,25L74,9L70,34L92,21L80,42L102,45L80,54L94,72L71,64L76,90L57,74L52,100L45,73L27,90L31,63L7,71L21,53L-1,45L21,39L6,19L30,33L27,6L44,25Z" fill="#00A6EF"/>'
 '<path d="M50,26L55,42L70,38L59,50L70,62L55,58L50,74L45,58L30,62L41,50L30,38L45,42Z" fill="#FBC001"/></svg>')
SPKG=('<g stroke="#FBC001" stroke-width="5" stroke-linecap="round">'
 '<path d="M8 24 L16 13"/><path d="M21 9 L24 -1"/><path d="M29 17 L39 12"/></g>')
RIBSVG=('<svg viewBox="0 0 300 44" preserveAspectRatio="none" aria-hidden="true">'
     '<path d="M0,0 L300,0 L288,22 L300,44 L0,44 L12,22 Z" fill="#00A6EF"/></svg>')
def UL(style=""): return (f'<svg class="uline" viewBox="0 0 300 20" preserveAspectRatio="none" aria-hidden="true"'
     f'{" style=\"%s\""%style if style else ""}><path d="M3,12 C70,2 190,19 297,5 C190,13 70,9 3,17 Z" fill="#DC1548"/></svg>')
def swatch(bd): return f'<svg class="sw" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true"><path d="{bd}" fill="#FBC001"/></svg>'
CSS=io.open('style.css',encoding='utf-8').read()

# ══════════════════ creative pieces ══════════════════
TILE=(f'<div class="ab tile" style="clip-path:{TEAR}"><div class="grain"></div>{BRP("bp")}{BRB("bb")}'
 f'<svg class="spk" viewBox="0 0 40 40" style="right:19%;top:16px;width:42px;height:42px" aria-hidden="true">{SPKG}</svg>'
 '<div class="corner" style="left:-8px;width:250px;height:210px;'
 '-webkit-mask-image:radial-gradient(120% 120% at 0% 100%,#000 55%,transparent 88%);'
 f'mask-image:radial-gradient(120% 120% at 0% 100%,#000 55%,transparent 88%)"><img src="{MARGS}" alt=""></div>'
 '<div class="corner" style="right:-8px;width:230px;height:190px;'
 '-webkit-mask-image:radial-gradient(120% 120% at 100% 100%,#000 55%,transparent 88%);'
 f'mask-image:radial-gradient(120% 120% at 100% 100%,#000 55%,transparent 88%)"><img src="{QUESO}" alt=""></div>'
 '<div class="core"><div class="kick" style="font-size:13px;color:#A8103A">Wed &ndash; Sun &middot; This week only</div>'
 '<h2 class="big" style="font-size:66px;color:var(--navy);margin-top:8px">Two Margs<br><span style="color:var(--pink)">+ A Dip</span></h2>'
 +UL("height:18px;width:340px;margin:6px auto 16px")+
 f'<div class="prices"><span class="pb">{swatch(BR1)}<span class="amt" style="font-size:54px">$25</span>'
 '<span class="lbl" style="font-size:15px">2 House Margs<br>+ Chips &amp; Guac or Queso</span></span></div>'
 '<div style="font-family:var(--s);font-weight:800;font-size:10.5px;letter-spacing:.08em;text-transform:uppercase;'
 'color:#A8103A;margin-top:14px">Not valid during Late Night Happy Hour &middot; Fri &amp; Sat 8&ndash;10pm</div>'
 '</div></div>')

POS=('<div class="ab pos">'
 f'<div class="mast">{BRP("bp")}{BRB("bb")}<img src="{WORDW}" alt="Uno Mas Tacos and Tequila"></div>'
 f'<div class="pblock" style="clip-path:{EDGE}">'
 '<h1 class="big" style="font-size:38pt;color:#FCFBFB">Two Margs<br>+ A Dip</h1></div>'
 '<div class="bd">'
 f'<div class="art" style="left:-.42in;top:.06in;width:2.6in"><img src="{MARGS}" alt=""></div>'
 f'<svg class="spk" viewBox="0 0 40 40" style="right:.9in;top:.1in;width:.32in;height:.32in" aria-hidden="true">{SPKG}</svg>'
 '<div style="margin-left:2.16in;margin-top:.2in;position:relative;z-index:12;text-align:left">'
 '<div style="font-family:var(--d);font-weight:700;font-size:64pt;line-height:.8;color:var(--navy)">$25</div>'
 '<div style="font-family:var(--d);font-weight:700;text-transform:uppercase;font-size:13pt;line-height:1.1;'
 'color:var(--navy);margin-top:.08in">2 House Margs<br>+ Chips &amp; Guac<br>or Chips &amp; Queso</div></div>'
 f'<div style="display:flex;justify-content:center;margin-top:.26in"><div class="ribbon">{RIBSVG}'
 '<b>Wed &ndash; Sun &middot; This week only</b></div></div>'
 f'<div class="art" style="left:1.1in;bottom:.92in;width:3.3in"><img src="{QUESO}" alt=""></div>'
 '<div style="margin-top:auto;position:relative;z-index:12">'
 '<div class="script" style="font-size:16pt">Start with the good stuff.'
 +UL("height:.12in;width:2.2in;margin:.01in auto 0")+'</div>'
 '<p class="fine" style="margin:.05in 0 .07in">Wed 2 Sep &ndash; Sun 6 Sep 2026. House margaritas only. No limit per visit. '
 '<b>Not valid 8&ndash;10pm Fri &amp; Sat during Late Night Happy Hour.</b></p></div></div>'
 '<div class="cta"><b>Ask your server.</b></div>'
 '<div class="foot"><b>Tacos. Margs. Brunch. Get a little lost.</b></div></div>')

EM=(f'<div class="ab em"><div class="hero2">{BRP("bp")}{BRB("bb")}<div class="grain"></div>'
 '<div style="position:relative;z-index:12">'
 '<div class="kick" style="font-size:11px;color:#A8103A">The Weekly Promo Drop</div>'
 '<h1 class="big" style="font-size:44px;color:var(--navy);margin-top:7px">Two Margs<br><span style="color:var(--pink)">+ A Dip</span></h1>'
 '<div style="font-family:var(--d);font-weight:700;font-size:62px;line-height:.85;color:var(--pink);margin-top:10px">$25</div>'
 '<div style="font-family:var(--d);font-weight:700;text-transform:uppercase;font-size:15px;color:var(--navy);margin-top:6px">'
 '2 House Margs + Chips &amp; Guac or Queso</div>'
 '<div style="font-family:var(--s);font-weight:800;font-size:10px;letter-spacing:.09em;text-transform:uppercase;'
 'color:#A8103A;margin-top:9px">Wed &ndash; Sun &middot; This week only</div></div></div>'
 '<div class="band"><b>Wed 2 Sep &ndash; Sun 6 Sep</b></div>'
 '<div class="body"><p>Two house margaritas and your pick of chips &amp; guacamole or chips &amp; queso blanco. '
 '<b>$25.</b></p>'
 '<p style="margin-top:12px">No code, no app, nothing to show us. Just ask your server &mdash; and there is no limit, '
 'so bring people.</p>'
 '<p style="margin-top:18px;text-align:center"><a class="btn" href="#">See the menu</a></p>'
 '<p style="margin-top:18px;font-size:11.5px;color:#6a7583;line-height:1.5">House margaritas only. No limit per visit. '
 'Not valid 8&ndash;10pm Friday &amp; Saturday during Late Night Happy Hour.</p></div></div>')

SMS=[("Tue 1 Sep","Announce &mdash; program only, no detail",
      "New Weekly Promo Drop lands tomorrow. Wed-Sun only. You'll want to be here.",75),
     ("Wed 2 Sep","Reveal",
      "This week's drop: 2 house margs + chips &amp; guac or queso, $25. Wed-Sun. Ask your server.",87),
     ("Sat 5 Sep","Last call",
      "Last call on the $25 drop: 2 house margs + your chips &amp; dip. Ends Sunday.",73)]

DEC=[("Dip choice &mdash; guac and queso, or include salsa?",
  "<b>Recommend guacamole and queso blanco only.</b> Salsa is the lightest of the three and does not carry the offer &mdash; "
  "guac and queso are what people actually want, and keeping it to two makes the choice easy to say out loud."),
 ("Late Night carve-out &mdash; confirm it goes on the piece",
  "<b>Recommend yes, and it is not really optional.</b> Late Night Happy Hour runs Fri and Sat 8&ndash;10pm with its own "
  "margarita pricing, and the two offers work against each other in that window. Without the line the floor has no rule "
  "and will improvise. It is on the poster, the tile and the email as drafted."),
 ("Chips &amp; Queso &mdash; verify on both printed menus",
  "The Lunch and Dinner PDFs already disagree with each other on the Chip &amp; Dip Trio, so it is worth a look at the "
  "individual dips before anything goes to print. Nothing on this piece quotes a menu price, but the floor still needs "
  "to ring it correctly."),
 ("Fourth bundle in five weeks &mdash; is that deliberate?",
  "Tests 2, 3 and now 5 are all bundles. The gift card was the one structurally different test, and it is the one you "
  "just told me worked. Not an objection &mdash; but if the Drop becomes &ldquo;there is always a bundle,&rdquo; the "
  "novelty that made it land wears off.")]

TIMELINE=[("Mon 31 Aug","Approve this page. Lock the dip choice and the Late Night carve-out.","Ramsey"),
 ("Tue 1 Sep","Announce SMS &mdash; program only, no detail. Brief the floor.","Ramsey / Claude"),
 ("Tue 1 Sep","Posters printed and on tables. Website tile pushed, gated Wed&ndash;Sun.","Team / Claude"),
 ("Wed 2 Sep","Reveal SMS and email. Offer goes live.","Claude drafts, Ramsey sends"),
 ("Wed 2 Sep","Meta ads live, if running paid.","Ramsey"),
 ("Sat 5 Sep","Last-call SMS.","Ramsey"),
 ("Sun 6 Sep","Offer ends at close.","&mdash;"),
 ("Mon 7 Sep","Log check average, redemption count and attach rate.","Claude")]

def piece(t,d,art,scale,h):
    return (f'<div class="piece"><div class="cap"><span class="t">{t}</span><span class="d">{d}</span></div>'
            f'<div class="frame"><div style="transform:scale({scale});transform-origin:top center;height:{h}">{art}</div></div></div>')

H=[]
A=H.append
A('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">')
A('<meta name="viewport" content="width=device-width,initial-scale=1"><title>Two Margs + A Dip</title>')
A("<style>@import url('https://fonts.googleapis.com/css2?family=Antonio:wght@400;600;700&family=Montserrat:wght@400;600;700;800;900&family=Yellowtail&display=swap');")
A(CSS+'</style></head><body>')
A('<button class="print" onclick="window.print()">Save as PDF</button>')

# header
A(f'<div class="site"><div class="wide"><img src="{WORDW}" alt="Uno Mas Tacos and Tequila">'
  '<nav><a href="#offer">The offer</a><a href="#creative">Creative</a><a href="#words">The words</a>'
  '<a href="#week">Run of week</a><a href="#decide">Before we build</a></nav></div></div>')

# hero
A('<div class="hero">'+BRP("a")+BRB("b")+
  f'<div class="art l"><img src="{MARGS}" alt=""></div><div class="art r"><img src="{GUAC}" alt=""></div>'
  '<div class="wrap inner"><div class="kick">The Weekly Promo Drop</div>'
  '<h1 class="big">Two Margs<br><em>+ A Dip</em></h1>'
  +UL()+
  '<div class="price">$25</div>'
  '<div class="sub">Two house margaritas<br>+ chips &amp; guac or chips &amp; queso</div>'
  f'<div class="ribbon">{RIBSVG}<b>Wed 2 Sep &ndash; Sun 6 Sep</b></div>'
  '<div class="askline">Just ask your server.</div></div></div>')

# offer
A('<section class="tint" id="offer"><div class="wrap"><div class="eyebrow">The detail</div>'
  '<h2>What it is, <span>exactly</span></h2>'
  '<p class="lede">Test five in the Weekly Promo Drop. Announced Tuesday with no detail, revealed Wednesday, '
  'runs through Sunday.</p><div class="rule"></div>'
  '<dl class="spec">'
  '<div><dt>Offer</dt><dd><b>Two house margaritas + your pick of Chips &amp; Guacamole or Chips &amp; Queso Blanco &mdash; $25</b></dd></div>'
  '<div><dt>Window</dt><dd>Wednesday 2 September &ndash; Sunday 6 September 2026, all day</dd></div>'
  '<div><dt>Exclusion</dt><dd><b>Not valid 8&ndash;10pm Friday and Saturday</b>, during Late Night Happy Hour</dd></div>'
  '<div><dt>Redemption</dt><dd>Ask your server. No code, no app, nothing to show.</dd></div>'
  '<div><dt>Limit</dt><dd><b>No limit.</b> Order it as many times as you like, per visit</dd></div>'
  '<div><dt>Drinks</dt><dd><b>House margaritas only.</b> Cadillac and flavored margs are not part of the offer</dd></div>'
  '<div><dt>Dips</dt><dd>Chips &amp; Guacamole or Chips &amp; Queso Blanco. Chips &amp; salsa is not included</dd></div>'
  '</dl></div></section>')

# how it works
A('<section><div class="wrap"><div class="eyebrow">How it works</div>'
  '<h2>Three things <span>to say</span></h2><div class="rule"></div>'
  '<div class="steps">'
  '<div class="step"><div class="n">1</div><h3>Just ask</h3><p>No code word this week, no app, nothing to show. '
  'A guest asks and the server rings it.</p></div>'
  '<div class="step"><div class="n">2</div><h3>Pick a dip</h3><p>Guacamole or queso blanco. Two choices so it is '
  'easy to say out loud and easy to remember.</p></div>'
  '<div class="step"><div class="n">3</div><h3>Again if you like</h3><p>No limit. Two more margs and another dip '
  'is another $25 &mdash; this is an upsell, not a coupon.</p></div>'
  '</div></div></section>')

# creative
A('<section class="mist" id="creative"><div class="wide"><div class="eyebrow">Creative</div>'
  '<h2>Where it <span>shows up</span></h2>'
  '<p class="lede">Three surfaces. All built on the illustrated promo system &mdash; the same one behind Weekend Special '
  'and Full Send. Menus stay clean type on white; promos are illustrated. Different jobs.</p><div class="rule"></div>'
  '<div class="showcase">'
  +piece("Website tile","Homepage, gated Wed&ndash;Sun",TILE,".60","320px")
  +piece("Table topper","5.5 &times; 8.5in, print",POS,".66","calc(8.5in * .66)")
  +piece("Email","Through Toast, 600px wide",EM,"1","auto")
  +'</div>'
  '<div class="callout"><b>One config entry ships the tile.</b> Add it to <code>src/config/weeklyPromo.ts</code> with '
  '<code>startISO 2026-09-02</code>, <code>endISO 2026-09-06</code> and <code>live: true</code>. If it overlaps a day '
  'special, the crossfade rotator handles it and this tile takes slide one.</div>'
  '</div></section>')

# words
A('<section class="tint" id="words"><div class="wrap"><div class="eyebrow">The words</div>'
  '<h2>Every message, <span>written</span></h2>'
  '<p class="lede">Toast prepends the restaurant name and appends the opt-out, so neither appears in the body. '
  'All three texts avoid the accented &aacute; in &ldquo;M&aacute;s&rdquo; and any curly quote or dash &mdash; those force a '
  'different encoding that cuts a message from 160 characters to 70.</p><div class="rule"></div>'
  '<div class="copygrid">'
  +''.join(f'<div class="cc"><div class="when">{d}</div><div class="role">{r}</div>'
           f'<div class="msg">{m}</div><div class="tech">{c} characters &middot; <b>single message</b></div></div>'
           for d,r,m,c in SMS)
  +'</div>'
  '<h2 style="margin-top:52px;font-size:26px">Email subject lines</h2>'
  '<ul class="plain">'
  '<li>Two margs and a dip. $25.</li>'
  '<li>This week: two margs and a dip</li>'
  '<li>Start with the good stuff</li>'
  '<li>The drop is live. Two margs + a dip.</li>'
  '</ul>'
  '<div class="callout"><b>Preheader:</b> &ldquo;Wednesday through Sunday. Ask your server &mdash; no code needed.&rdquo;</div>'
  '<h2 style="margin-top:52px;font-size:26px">Meta ads</h2>'
  '<ul class="plain">'
  '<li>Two house margs and your pick of chips &amp; guac or queso. $25, Wednesday through Sunday. Monroe Street, Spokane.'
  '<span>Primary text A</span></li>'
  '<li>The kind of order that turns into staying longer than you planned. Two margs, a dip, $25. This week only.'
  '<span>Primary text B</span></li>'
  '<li>Two Margs + A Dip &mdash; $25<span>Headline</span></li>'
  '<li>Wed&ndash;Sun. Ask your server.<span>Description</span></li>'
  '<li>Learn More<span>Call to action &mdash; not Order Now, this is dine-in</span></li>'
  '</ul></div></section>')

# floor rules
A('<section class="deep"><div class="wrap"><div class="eyebrow">For the floor</div>'
  '<h2>Brief this, <span>don&rsquo;t just post it</span></h2><div class="rule" style="background:var(--yel)"></div>'
  '<ul class="rules">'
  '<li><b>Two house margs plus one chips &amp; dip &mdash; guacamole or queso &mdash; for $25.</b></li>'
  '<li><b>Chips &amp; salsa is not in the offer.</b> If a guest asks, it is guac or queso.</li>'
  '<li><b>Not available 8&ndash;10pm Friday and Saturday.</b> Late Night Happy Hour has its own margarita pricing. '
  'If someone asks in that window, point them at Late Night instead.</li>'
  '<li><b>House margaritas only.</b> Cadillac and flavored margs are not part of the offer.</li>'
  '<li><b>No limit.</b> A table can run it as many times as they want. Two more margs and another dip is another $25 &mdash; '
  'say it.</li>'
  '<li><b>No code word this week.</b> They just ask.</li>'
  '</ul></div></section>')

# run of week
A('<section id="week"><div class="wrap"><div class="eyebrow">Logistics</div>'
  '<h2>Run of <span>the week</span></h2><div class="rule"></div>'
  '<table class="tl"><thead><tr><th>When</th><th>What</th><th>Who</th></tr></thead><tbody>'
  +''.join(f'<tr><td>{w}</td><td>{x}</td><td>{y}</td></tr>' for w,x,y in TIMELINE)
  +'</tbody></table></div></section>')

# decisions
A('<section class="mist" id="decide"><div class="wrap"><div class="eyebrow">Before we build</div>'
  '<h2>Four things <span>we need settled</span></h2>'
  '<p class="lede">Nothing here is live and nothing is printed. Two of these change the offer itself.</p>'
  '<div class="rule"></div>'
  +''.join(f'<div class="dec"><div class="q">{q}</div><div class="r">{r}</div></div>' for q,r in DEC)
  +'</div></section>')

# measurement + assets
A('<section class="tint"><div class="wrap"><div class="eyebrow">Afterwards</div>'
  '<h2>What we <span>learn from it</span></h2>'
  '<p class="lede">Four tests have run and none has a number attached. That is the real gap, not the creative.</p>'
  '<div class="rule"></div>'
  '<ul class="plain" style="margin-top:26px">'
  '<li>Average check Wednesday&ndash;Sunday against the same days the week before<span>The number that says whether it worked</span></li>'
  '<li>Redemption count<span>How many actually ordered it</span></li>'
  '<li>Attach rate<span>Did they add the dip, or swap it for something they would have ordered anyway</span></li>'
  '<li>Which dip they picked<span>Decides whether guac or queso leads the creative next time</span></li>'
  '</ul>'
  '<div class="callout">The Toast dashboard is the tool for this, but <b>its API credentials currently fail '
  'authentication</b> &mdash; so this will be a manual pull unless that gets fixed first. Worth an hour before Wednesday.</div>'
  '<div class="callout"><b>No new artwork was needed.</b> The margaritas and the dip bowls are cropped from the '
  'Weekend Special poster, the only print-resolution illustrated asset in the library. There is still no standalone '
  'illustration of a single chips &amp; dip &mdash; it is on the generation backlog, and until it exists any dip artwork '
  'is a crop out of that one poster.</div>'
  '</div></section>')

A('<footer class="pg"><div class="wrap"><span class="sc">Get a little lost.</span>'
  'Uno M&aacute;s Tacos &amp; Tequila &middot; 2020 N Monroe St, Suite C, Spokane<br>'
  'Internal review page &mdash; nothing on it is live or printed. Drafted 31 August 2026.</div></footer>')
A('</body></html>')
io.open('promo-overview.html','w',encoding='utf-8').write("\n".join(H))
print("written", sum(len(x) for x in H))
