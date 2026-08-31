import io, random
random.seed(41)
B="https://res.cloudinary.com/drxrfyq9i/image/upload"
SRC="uno-mas/approved-assets/photos/promo/20260814_UM_PROMO_WeekendSpecial_Portrait"
MARGS=f"{B}/c_crop,x_105,y_1880,w_1700,h_1270/c_fit,w_1400,f_png/{SRC}"
QUESO=f"{B}/c_crop,x_2180,y_3120,w_720,h_540/c_fit,w_700,f_png/{SRC}"
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
BRP='<svg class="brst bp" viewBox="0 0 100 100" aria-hidden="true"><path d="M50,2L57,24L72,10L68,32L90,22L78,40L100,44L78,52L92,68L70,62L74,86L56,72L52,96L44,72L28,88L30,62L8,70L22,52L0,44L22,38L8,20L30,32L28,8L44,24Z" fill="#DC1548"/></svg>'
BRB=('<svg class="brst bb" viewBox="0 0 100 100" aria-hidden="true">'
 '<path d="M50,0L58,25L74,9L70,34L92,21L80,42L102,45L80,54L94,72L71,64L76,90L57,74L52,100L45,73L27,90L31,63L7,71L21,53L-1,45L21,39L6,19L30,33L27,6L44,25Z" fill="#00A6EF"/>'
 '<path d="M50,26L55,42L70,38L59,50L70,62L55,58L50,74L45,58L30,62L41,50L30,38L45,42Z" fill="#FBC001"/></svg>')
SPKG=('<g stroke="#FBC001" stroke-width="5" stroke-linecap="round">'
 '<path d="M8 24 L16 13"/><path d="M21 9 L24 -1"/><path d="M29 17 L39 12"/></g>')
RIB=('<svg class="ribsvg" viewBox="0 0 300 44" preserveAspectRatio="none" aria-hidden="true">'
     '<path d="M0,0 L300,0 L288,22 L300,44 L0,44 L12,22 Z" fill="#00A6EF"/></svg>')
def UL(style): return (f'<svg class="uline" viewBox="0 0 300 20" preserveAspectRatio="none" aria-hidden="true" style="{style}">'
     '<path d="M3,12 C70,2 190,19 297,5 C190,13 70,9 3,17 Z" fill="#DC1548"/></svg>')
def swatch(bd): return f'<svg class="sw" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true"><path d="{bd}" fill="#FBC001"/></svg>'

SMS=[("Tue 1 Sep","Announce &mdash; program only",
      "New Weekly Promo Drop lands tomorrow. Wed-Sun only. You'll want to be here.",75),
     ("Wed 2 Sep","Reveal",
      "This week's drop: 2 house margs + chips &amp; guac or queso, $25. Wed-Sun. Ask your server.",87),
     ("Sat 5 Sep","Last call",
      "Last call on the $25 drop: 2 house margs + your chips &amp; dip. Ends Sunday.",73)]

CSS = io.open('style.css',encoding='utf-8').read()

TILE=(f'<div class="ab tile" style="clip-path:{TEAR}"><div class="grain"></div>{BRP}{BRB}'
 f'<svg class="spk" viewBox="0 0 40 40" style="right:19%;top:16px;width:42px;height:42px" aria-hidden="true">{SPKG}</svg>'
 '<div class="corner" style="left:-8px;width:250px;height:210px;'
 '-webkit-mask-image:radial-gradient(120% 120% at 0% 100%,#000 55%,transparent 88%);'
 f'mask-image:radial-gradient(120% 120% at 0% 100%,#000 55%,transparent 88%)"><img src="{MARGS}" alt=""></div>'
 '<div class="corner" style="right:-8px;width:230px;height:190px;'
 '-webkit-mask-image:radial-gradient(120% 120% at 100% 100%,#000 55%,transparent 88%);'
 f'mask-image:radial-gradient(120% 120% at 100% 100%,#000 55%,transparent 88%)"><img src="{QUESO}" alt=""></div>'
 '<div class="core"><div class="kick" style="font-size:13px;color:#8A1030">Wed &ndash; Sun &middot; This week only</div>'
 '<h2 class="big" style="font-size:66px;color:var(--nd);margin-top:8px">Two Margs<br><span style="color:var(--pink)">+ A Dip</span></h2>'
 +UL("height:18px;width:340px;margin:6px auto 16px")+
 f'<div class="prices"><span class="pb">{swatch(BR1)}<span class="amt" style="font-size:54px">$25</span>'
 '<span class="lbl" style="font-size:15px">2 House Margs<br>+ Chips &amp; Guac or Queso<em>REG UP TO $33</em></span></span></div>'
 '<div style="font-family:var(--s);font-weight:800;font-size:10.5px;letter-spacing:.08em;text-transform:uppercase;'
 'color:#8A1030;margin-top:14px">Not valid during Late Night Happy Hour &middot; Fri &amp; Sat 8&ndash;10pm</div>'
 '</div></div>')

POS=('<div class="ab pos">'
 f'<div class="mast">{BRP}{BRB}<img src="{WORDW}" alt="Uno Mas Tacos and Tequila"></div>'
 f'<div class="pblock" style="clip-path:{EDGE}">'
 '<h1 class="big" style="font-size:38pt;color:#FCFBFB">Two Margs<br>+ A Dip</h1></div>'
 '<div class="bd">'
 f'<div class="art" style="left:-.42in;top:.06in;width:2.6in"><img src="{MARGS}" alt=""></div>'
 f'<svg class="spk" viewBox="0 0 40 40" style="right:.9in;top:.1in;width:.32in;height:.32in" aria-hidden="true">{SPKG}</svg>'
 '<div style="margin-left:2.16in;margin-top:.14in;position:relative;z-index:12;text-align:left">'
 '<div style="font-family:var(--d);font-weight:700;font-size:64pt;line-height:.8;color:var(--nd)">$25</div>'
 '<div style="font-family:var(--d);font-weight:700;text-transform:uppercase;font-size:13pt;line-height:1.1;'
 'color:var(--nd);margin-top:.06in">2 House Margs<br>+ Chips &amp; Guac<br>or Chips &amp; Queso</div>'
 '<div style="font-family:var(--s);font-weight:800;font-size:7pt;letter-spacing:.07em;text-transform:uppercase;'
 'color:#8A1030;margin-top:.08in">Up to $33 &agrave; la carte</div></div>'
 f'<div style="display:flex;justify-content:center;margin-top:.2in"><div class="ribbon">{RIB}'
 '<b style="font-size:11pt">Wed &ndash; Sun &middot; This week only</b></div></div>'
 f'<div class="art" style="left:1.1in;bottom:.92in;width:3.3in"><img src="{QUESO}" alt=""></div>'
 '<div style="margin-top:auto;position:relative;z-index:12">'
 '<div class="script" style="font-size:16pt">Start with the good stuff.'
 +UL("height:.12in;width:2.2in;margin:.01in auto 0")+'</div>'
 '<p class="fine" style="margin:.05in 0 .07in">Wed 2 Sep &ndash; Sun 6 Sep 2026. House margaritas only. No limit per visit. '
 '<b>Not valid 8&ndash;10pm Fri &amp; Sat during Late Night Happy Hour.</b></p></div></div>'
 '<div class="cta"><b>Ask your server.</b></div>'
 '<div class="foot"><b>Tacos. Margs. Brunch. Get a little lost.</b></div></div>')

EM=(f'<div class="ab em"><div class="hero">{BRP}{BRB}<div class="grain"></div>'
 '<div style="position:relative;z-index:12">'
 '<div class="kick" style="font-size:11px;color:#8A1030">The Weekly Promo Drop</div>'
 '<h1 class="big" style="font-size:44px;color:var(--nd);margin-top:7px">Two Margs<br><span style="color:var(--pink)">+ A Dip</span></h1>'
 '<div style="font-family:var(--d);font-weight:700;font-size:62px;line-height:.85;color:var(--pink);margin-top:10px">$25</div>'
 '<div style="font-family:var(--d);font-weight:700;text-transform:uppercase;font-size:15px;color:var(--nd);margin-top:6px">'
 '2 House Margs + Chips &amp; Guac or Queso</div>'
 '<div style="font-family:var(--s);font-weight:800;font-size:10px;letter-spacing:.09em;text-transform:uppercase;'
 'color:#8A1030;margin-top:9px">Wed &ndash; Sun &middot; This week only</div></div></div>'
 '<div class="band"><b>Wed 2 Sep &ndash; Sun 6 Sep</b></div>'
 '<div class="body"><p>Two house margaritas and your pick of chips &amp; guacamole or chips &amp; queso blanco '
 '&mdash; <b>$25</b>. Up to $33 if you ordered it off the menu.</p>'
 '<p style="margin-top:12px">No code, no app, nothing to show us. Just ask your server &mdash; and there is no limit, so bring people.</p>'
 '<p style="margin-top:18px;text-align:center"><a class="btn" href="#">See the menu</a></p>'
 '<p style="margin-top:18px;font-size:11.5px;color:#6a7583;line-height:1.5">House margaritas only. No limit per visit. '
 'Not valid 8&ndash;10pm Friday &amp; Saturday during Late Night Happy Hour.</p></div></div>')

DEC=[("Dip choice &mdash; guac and queso only, or include salsa?",
  "<b>Recommend guac ($6) + queso ($8) only.</b> Two house margs are $25 on their own, so the dip is what makes this "
  "an offer. Salsa at $4 saves the guest $4 &mdash; reads like nothing, costs you the same margin. Guac saves $6, "
  "queso saves $8. Those two land."),
 ("Late Night carve-out &mdash; in or out?",
  "<b>Recommend in, and it is not really optional.</b> After 8pm Fri/Sat margs drop to $6, so the contents are worth $20 max "
  "and a $25 bundle would cost the guest <b>$5 more than the menu</b>. Without the line the floor either refuses the sale "
  "or a guest does the math and feels misled."),
 ("Chips &amp; Queso price &mdash; verify against both printed menus",
  "The &ldquo;up to $33&rdquo; claim rests on Chips &amp; Queso being $8. Related unresolved conflict: the Lunch PDF prices the "
  "Chip &amp; Dip Trio at $16 and the Dinner PDF at $15, so the printed menus already disagree with each other somewhere."),
 ("Fourth bundle in five weeks &mdash; is that the plan?",
  "Tests 2, 3 and now this are all bundles. The gift card was the one structurally different test and it worked. "
  "Not an objection &mdash; but if the Drop becomes &ldquo;there is always a bundle,&rdquo; the novelty that made it work erodes.")]

VALUE=[("Chips &amp; Guacamole","$6","$31","$25","$6","19%","good"),
       ("Chips &amp; Queso Blanco","$8","$33","$25","$8","24%","good"),
       ("Chips &amp; Salsa <span class='warnc'>(recommend excluding)</span>","$4","$29","$25","$4","14%","warnc")]

TIMELINE=[("Mon 31 Aug","Approve this doc. Lock the dip choice, the carve-out and the marg rules.","Ramsey"),
 ("Tue 1 Sep","Announce SMS &mdash; program only, no detail. Brief the floor.","Ramsey / Claude"),
 ("Tue 1 Sep","Posters printed and on tables. Website tile pushed, gated Wed&ndash;Sun.","Team / Claude"),
 ("Wed 2 Sep","Reveal SMS + email. Offer goes live.","Claude drafts, Ramsey sends"),
 ("Wed 2 Sep","Meta ads live, if running paid.","Ramsey"),
 ("Sat 5 Sep","Last-call SMS.","Ramsey"),
 ("Sun 6 Sep","Offer ends at close.","&mdash;"),
 ("Mon 7 Sep","Log check average, redemption count and attach rate to the executions log.","Claude")]

def dec(q,r): return f'<div class="dec"><div class="q">{q}</div><div class="r">{r}</div></div>'

html=('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
 '<meta name="viewport" content="width=device-width,initial-scale=1"><title>Two Margs + A Dip</title>'
 "<style>@import url('https://fonts.googleapis.com/css2?family=Antonio:wght@400;600;700&family=Montserrat:wght@400;600;700;800;900&family=Yellowtail&display=swap');"
 +CSS+'</style></head><body>'
 '<header class="pg"><h1>The Weekly Promo Drop &mdash; Two Margs + A Dip</h1>'
 '<div class="s">$25 &middot; Wed 2 Sep &ndash; Sun 6 Sep 2026 &middot; team review, nothing built yet</div>'
 '<div class="tools"><button onclick="window.print()">&#8853; Print / Save as PDF</button></div></header><main>'
 '<div class="note stop"><b>Read this first: nothing here is live and nothing is printed.</b> This is the review '
 'package. Six decisions are open below &mdash; two of them (the dip choice and the Late Night carve-out) change '
 'the offer itself, so they need answering before any of this gets made.</div>'
 '<h2 class="sec">The offer</h2>'
 '<p class="lede">Test 5 in the Weekly Promo Drop sequence. Announced Tuesday with no detail, revealed Wednesday, runs Wed&ndash;Sun.</p>'
 '<table class="d"><tbody>'
 '<tr><td style="width:170px"><b>Offer</b></td><td><b>2 House Margaritas + your pick of Chips &amp; Guacamole or Chips &amp; Queso Blanco &mdash; $25</b></td></tr>'
 '<tr><td><b>Window</b></td><td>Wed 2 Sep &ndash; Sun 6 Sep 2026, all day</td></tr>'
 '<tr><td><b>Exclusion</b></td><td class="bad">Not valid 8&ndash;10pm Fri &amp; Sat during Late Night Happy Hour</td></tr>'
 '<tr><td><b>Redemption</b></td><td>Ask your server. No code, no app, nothing to show.</td></tr>'
 '<tr><td><b>Limit</b></td><td><b>No limit</b> &mdash; order it as many times as you like, per visit</td></tr>'
 '<tr><td><b>Drinks</b></td><td><b>House margaritas only.</b> No Cadillac, no flavored upgrades at the offer price.</td></tr>'
 '</tbody></table>'
 '<h2 class="sec">Decisions needed <span>before anything is made</span></h2>'
 +''.join(dec(q,r) for q,r in DEC)+
 '<h2 class="sec">Floor rules <span>&mdash; the staff version</span></h2>'
 '<div class="note"><b>Brief this, do not just post it.</b><br>'
 '&bull; The offer is <b>two house margs plus one chips &amp; dip &mdash; guac or queso &mdash; for $25</b>.<br>'
 '&bull; <b>Chips &amp; salsa is not in the offer.</b> If a guest asks, it is guac or queso.<br>'
 '&bull; <b>Not available 8&ndash;10pm Friday and Saturday.</b> Late Night has $6 margs, which beats this on the drinks '
 'alone &mdash; if someone asks in that window, tell them Late Night pricing is better and sell that instead.<br>'
 '&bull; <b>House margaritas only.</b> Cadillac and flavored margs are not part of the offer &mdash; those stay full price.<br>'
 '&bull; <b>No limit.</b> A table can run it as many times as they want &mdash; two more margs, another dip, another $25.<br>'
 '&bull; No code word this week. Just ask.</div>'
 '<h2 class="sec">Website tile</h2>'
 '<p class="lede">Drops into the existing <code>PromoSlot</code> as a weekly-promo entry, gated Wed&ndash;Sun. '
 'If it overlaps a day special, the crossfade rotator you approved handles it &mdash; this tile takes slide one.</p>'
 f'<div class="stage" style="padding:24px"><div style="transform:scale(.62);transform-origin:top center;height:330px">{TILE}</div></div>'
 '<div class="note"><b>One config entry ships it:</b> add to <code>src/config/weeklyPromo.ts</code> with '
 '<code>startISO 2026-09-02</code>, <code>endISO 2026-09-06</code>, <code>live: true</code>. '
 'The <code>live</code> flag exists precisely so a dated promo cannot appear before its creative does.</div>'
 '<h2 class="sec">Poster <span>&mdash; 5.5 &times; 8.5in table topper</span></h2>'
 '<p class="lede">Illustrated system, matching Weekend Special and Full Send. Note the deliberate split: '
 '<b>promos are illustrated, menus are clean type on white.</b> Two different jobs.</p>'
 f'<div class="stage" style="padding:24px"><div style="transform:scale(.66);transform-origin:top center;height:calc(8.5in * .66)">{POS}</div></div>'
 '<h2 class="sec">SMS</h2>'
 '<p class="lede">Toast prepends the restaurant name and appends the opt-out, so neither appears in the body. '
 'All three avoid the accented &aacute; in &ldquo;M&aacute;s&rdquo; and any curly quote or en dash &mdash; those force UCS-2, '
 'which cuts a segment from 160 characters to 70 and roughly doubles the send cost.</p>'
 '<div class="cards">'
 +''.join(f'<div class="card"><div class="hd"><span class="tag">{d}</span><span class="nm">{t}</span></div>'
          f'<div class="bd"><pre class="sms">{m}</pre>'
          f'<div class="meta">{c} chars &middot; <b class="ok">GSM-7</b> &middot; <b class="ok">1 segment</b></div></div></div>'
          for d,t,m,c in SMS)
 +'</div>'
 '<h2 class="sec">Email</h2>'
 '<p class="lede">Goes through Toast, not Klaviyo &mdash; same channel as the previous four tests. 600px wide.</p>'
 '<table class="d"><thead><tr><th>Subject line options</th><th class="num">Chars</th></tr></thead><tbody>'
 '<tr><td>Two margs and a dip. $25.</td><td class="num">25</td></tr>'
 '<tr><td>This week: $25 gets you two margs and a dip</td><td class="num">43</td></tr>'
 '<tr><td>Start with the good stuff &mdash; $25</td><td class="num">30</td></tr>'
 '<tr><td>The drop is live. Two margs + a dip, $25.</td><td class="num">42</td></tr>'
 '</tbody></table>'
 '<div class="note"><b>Preheader:</b> &ldquo;Wednesday through Sunday. Ask your server &mdash; no code needed.&rdquo;</div>'
 f'<div class="stage" style="padding:24px">{EM}</div>'
 '<h2 class="sec">Meta ads copy</h2>'
 '<table class="d"><thead><tr><th style="width:110px">Field</th><th>Copy</th></tr></thead><tbody>'
 '<tr><td><b>Primary A</b></td><td>Two house margs and your pick of chips &amp; guac or queso. $25, Wednesday through Sunday. '
 'Up to $33 if you ordered it off the menu. Monroe Street, Spokane.</td></tr>'
 '<tr><td><b>Primary B</b></td><td>The kind of order that turns into staying longer than you planned. Two margs, a dip, $25. '
 'This week only.</td></tr>'
 '<tr><td><b>Headline</b></td><td>Two Margs + A Dip &mdash; $25</td></tr>'
 '<tr><td><b>Description</b></td><td>Wed&ndash;Sun. Ask your server.</td></tr>'
 '<tr><td><b>CTA</b></td><td>Learn More &nbsp;<span style="color:var(--mut)">(not Order Now &mdash; this is dine-in)</span></td></tr>'
 '</tbody></table>'
 '<h2 class="sec">Run of week</h2>'
 '<table class="d"><thead><tr><th style="width:110px">When</th><th>What</th><th style="width:170px">Who</th></tr></thead><tbody>'
 +''.join(f'<tr><td><b>{w}</b></td><td>{x}</td><td style="color:var(--mut)">{y}</td></tr>' for w,x,y in TIMELINE)
 +'</tbody></table>'
 '<h2 class="sec">What to measure</h2>'
 '<div class="note"><b>Four tests have run and none has a number attached to it.</b> That is the real gap, not the creative. '
 'For this one, capture: <b>average check</b> Wed&ndash;Sun vs the same days last week &middot; <b>redemption count</b> '
 '&middot; <b>attach rate</b> &mdash; did they add the dip, or swap it for something they would have ordered anyway '
 '&middot; <b>which dip</b> they picked, since that decides whether guac or queso leads the creative next time.<br><br>'
 'The Toast dashboard at <code>~/projects/unomas-toast-dashboard</code> is the tool, but <b>its API credentials '
 'currently fail auth</b>, so this will be a manual pull unless that gets fixed first.</div>'
 '<h2 class="sec">Assets <span>&mdash; what exists and what doesn&rsquo;t</span></h2>'
 '<div class="note"><b>No new artwork was needed.</b> The margaritas and the single dip bowl are cropped from '
 '<code>20260814_UM_PROMO_WeekendSpecial_Portrait</code> (3506&times;4381), the only print-resolution illustrated asset '
 'in the library. The single-bowl crop yields 720&times;540 &mdash; enough for the 2in element used here, not enough to go bigger.<br><br>'
 '<b>The gap:</b> there is still no standalone illustration of a single chips &amp; dip, or of chips &amp; guacamole '
 'specifically. Both are on the generation backlog in <code>marketing/chatgpt-illustration-prompt.md</code>. '
 'Until that is filled, any dip artwork is a crop out of one poster.</div>'
 '</main></body></html>')
io.open('promo-overview.html','w',encoding='utf-8').write(html)
print("written",len(html))
