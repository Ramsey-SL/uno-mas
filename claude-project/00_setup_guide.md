# Uno Más — Claude Project Setup Guide

## What This Is

This folder contains everything you need to build a dedicated Claude project at claude.ai that functions as your Uno Más marketing and research assistant. Once set up, every conversation in the project automatically has full brand context — voice, menu, personas, performance data, SEO intel, and campaign templates.

---

## Setup Steps (Takes ~10 minutes)

### Step 1 — Create a New Project
1. Go to **claude.ai** and sign in
2. Click **"Projects"** in the left sidebar
3. Click **"Create project"**
4. Name it: **Uno Más — Marketing Assistant**

### Step 2 — Paste the Project Instructions
1. Inside the new project, click **"Edit project instructions"** (or the pencil icon)
2. Open the file `01_PROJECT_INSTRUCTIONS.md` from this folder
3. Copy the entire contents and paste it into the instructions field
4. Save

### Step 3 — Upload the Knowledge Files
1. Inside the project, click **"Add content"** or the upload icon
2. Upload each of the following files (in order):

| # | File | Why It Matters |
|---|---|---|
| 02 | `02_BRAND_INTELLIGENCE_MASTER.md` | The full brand guide — voice, positioning, audience, proof points, goals |
| 03 | `03_MESSAGING_FRAMEWORK.md` | StoryBrand map, narrative structure, approved taglines |
| 04 | `04_MENU_AND_OFFERS.md` | Complete menu with accurate pricing — reference before any product copy |
| 05 | `05_VENUE_AND_OPERATIONS.md` | Hours, venue details, team, operational facts |
| 06 | `06_AUDIENCE_PERSONAS.md` | Six personas with tone calibration by channel |
| 07 | `07_PERFORMANCE_DATA.md` | What content works, benchmarks, top post analysis |
| 08 | `08_SEO_KEYWORD_RESEARCH.md` | Keyword targets, competitive gaps, AI search strategy |
| 09 | `09_CAMPAIGN_TEMPLATES.md` | Ready-to-fill templates for social, email, SMS, reviews |

### Step 4 — Test It
Start a conversation and ask:
> "Write 3 Instagram captions for the dinner menu. One atmosphere-led, one food-forward, one Mezzanine tease."

If the response sounds like Uno Más (short sentences, no corporate language, Spokane pride, correct accent on the brand name), you're live.

---

## What the Assistant Can Do

**Content & Copy**
- Instagram captions, Reels scripts, Stories copy
- Klaviyo email campaigns and SMS
- Meta and Google ad copy
- Review responses (Google, Yelp) in under 100 words
- Blog posts and SEO web copy
- Menu callout copy and promo descriptions

**Strategy**
- Weekly and monthly content calendar planning
- Campaign briefs and promotional concepts
- Mezzanine event marketing and inquiry responses
- Loyalty campaign strategy (Uno Más Rewards: The Cantina Club)

**Research**
- Competitor analysis (Cochinito, Borracho, Table 13, etc.)
- SEO recommendations
- Social trend analysis
- Performance review and content recommendations

**Operations**
- Team and vendor communications
- Event proposals
- Process docs and templates

---

## Tips for Getting the Best Results

**Be specific about channel and audience:**
> "Write an Instagram caption for The Mezzanine, targeting corporate event planners."

**Specify the tone you want:**
> "Make it dinner-menu energy — confident and elevated, not patio casual."

**Attach context when you have it:**
> "Here's a photo of the Espresso Margarita — write a caption."

**Ask for iterations:**
> "Give me 3 versions. One punchy, one story-driven, one with a question hook."

**Flag what's currently active:**
> "We're running a Father's Day promotion this weekend — weave that in."

---

## Keeping It Current

The knowledge files are a snapshot. When things change, update the source files in `Uno Mas Marketing HQ/00_KNOWLEDGE_CENTER/` and re-upload the relevant files to the Claude project.

**Things most likely to change:**
- Menu items and pricing → re-upload `04_MENU_AND_OFFERS.md`
- Hours or venue operations → re-upload `05_VENUE_AND_OPERATIONS.md`
- Active campaigns and promotions → mention in the conversation or add a note to the project instructions
- Performance benchmarks → re-upload `07_PERFORMANCE_DATA.md` periodically

---

## Files in This Folder

```
Claude-Project/
├── 00_SETUP_GUIDE.md              ← You are here
├── 01_PROJECT_INSTRUCTIONS.md     ← Paste into Claude project settings
├── 02_BRAND_INTELLIGENCE_MASTER.md
├── 03_MESSAGING_FRAMEWORK.md
├── 04_MENU_AND_OFFERS.md
├── 05_VENUE_AND_OPERATIONS.md
├── 06_AUDIENCE_PERSONAS.md
├── 07_PERFORMANCE_DATA.md
├── 08_SEO_KEYWORD_RESEARCH.md
└── 09_CAMPAIGN_TEMPLATES.md
```

---

*Built by Strategy Labs for Ramsey Pruchnic — Uno Más Tacos & Tequila*
*June 2026*
