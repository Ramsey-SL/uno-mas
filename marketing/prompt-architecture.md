# Uno Mas Creative Studio — AI Prompt Architecture

_Last updated: 2026-05-01_

## Purpose

This document defines how the Uno Mas Creative Studio app composes prompts for AI image generation (Gemini 2.5 Flash Image, Imagen 4, etc.). The goal: brand-consistent creative output produced from structured user briefs combined with stored brand context, with no user-written prompts.

## Core Principle

The user never writes a prompt. The user fills a structured brief. The app composes the prompt from four independent input layers, runs it through the model, and returns a set of variations. Every input is stored separately for reproducibility and refinement.

## The Four-Layer Architecture

```
Layer 1: Brand Context        (set once, in Settings)
   ↓
Layer 2: Brief Form           (filled per generation)
   ↓
Layer 3: Reference Assets     (selected from Asset Library)
   ↓
Layer 4: Format Constraints   (set by channel selection)
   ↓
Composed Prompt → Image Model → 4 Variations → Refinement Loop
```

Each layer is stored separately in the database so outputs are auditable, reproducible, and editable later.

---

## Layer 1: Brand Context

Set once in Settings. Updated rarely. Auto-injected into every generation.

```json
{
  "brand_name": "Uno Mas",
  "photography_style": "Editorial lifestyle photography. Warm, inviting, lived-in but elevated. Shallow depth of field. Natural light strongly preferred over artificial. Shot on 35mm film aesthetic. Never sterile, never over-edited, never stock-looking.",
  "color_palette": "Terracotta (#C75D3A), warm cream (#F5E8D7), deep teal (#1A4D4B), warm gold accents, weathered wood tones",
  "settings_description": "Modern Mexican taqueria. Indoor: warm wood, leather banquettes, hanging plants, exposed brick. Outdoor: string-lit patio, terra cotta tiles, succulents.",
  "mood_baseline": "Lively, social, sophisticated-but-approachable, celebratory",
  "avoid_global": "Stock photography aesthetic, heavy filters, oversaturation, sterile lighting, generic restaurant imagery, AI-generated text, fake logos, distorted hands or faces"
}
```

---

## Layer 2: Brief Form

Filled per generation. Captures user intent.

```json
{
  "channel": "instagram_square",
  "goal": "Promote new spring mezcal margarita menu",
  "subject": "Three new mezcal margaritas launching this week",
  "mood": ["vibrant", "fresh", "celebratory"],
  "time_of_day": "golden_hour",
  "text_overlay_planned": true,
  "text_overlay_position": "top",
  "required_props": "Fresh lime garnish, salt rim, condensation on glasses",
  "reference_asset_ids": ["uuid-1", "uuid-2", "uuid-3"],
  "avoid_specific": ""
}
```

---

## Layer 3: Reference Assets

User selects 0–5 references from the Asset Library. Each reference's metadata is auto-pulled and used as conditioning context.

Rules:

- Style references (mood, lighting, color) are passed with weight ~0.5
- Composition references are passed with weight ~0.7
- Logos are NEVER used as references — they will be composited separately in the post-generation step
- Maximum 5 references per generation; more creates prompt confusion

---

## Layer 4: Format Constraints

Set by channel selection. Determines aspect ratio, composition behavior, and overlay reservation.

```javascript
const formatConstraints = {
  instagram_square: {
    aspect: "1:1",
    dimensions: "1080x1080",
    composition: "Centered square composition, balanced negative space"
  },
  instagram_story: {
    aspect: "9:16",
    dimensions: "1080x1920",
    composition: "Vertical 9:16, subject in upper-middle, leave bottom third clean for sticker/CTA placement"
  },
  instagram_reel_cover: {
    aspect: "9:16",
    dimensions: "1080x1920",
    composition: "Vertical 9:16, subject framed in middle-third, leave top 20% and bottom 20% clean"
  },
  email_header: {
    aspect: "16:9",
    dimensions: "1200x675",
    composition: "Horizontal 16:9, subject anchored on the right two-thirds, left third clean for headline"
  },
  web_banner: {
    aspect: "21:9",
    dimensions: "2100x900",
    composition: "Wide 21:9, subject right-anchored, large negative space on the left for headline and CTA"
  },
  web_blog_hero: {
    aspect: "16:9",
    dimensions: "1600x900",
    composition: "Horizontal 16:9, balanced composition, room at the bottom for caption overlay"
  }
};
```

---

## The Prompt Template

```text
{photography_style}

Subject: {subject_description} at {brand_name}, a {settings_short}.
{required_props_clause}

Composition: {composition_for_format}. {text_overlay_clause}

Lighting & atmosphere: {time_of_day_lighting}. {settings_full}.

Color palette: {color_palette}.

Mood: {mood_baseline}, with emphasis on {brief_mood}.

Style consistent with the brand's established photography: {photography_style_short}.

Quality: Photorealistic, high detail, professional editorial food photography.
```

---

## Composed Example

**Input:** Spring mezcal margarita promo for IG square, golden hour, mood: vibrant/fresh/celebratory.

**Composed prompt:**

```text
Editorial lifestyle photography. Warm, inviting, lived-in but elevated. Shallow depth of field. Natural light. Shot on 35mm film aesthetic.

Subject: Three vibrant mezcal margaritas in coupe glasses arranged on a warm wood table at Uno Mas, a modern Mexican taqueria. Fresh lime garnish, salt rims, visible condensation on the glasses.

Composition: Centered square composition, slightly overhead 45-degree angle, shallow depth of field with rear glass softly out of focus. Clean negative space in the top third of the frame for text overlay.

Lighting & atmosphere: Soft golden hour light from the left, warm afternoon glow. Outdoor string-lit patio in the background, blurred green plants and terra cotta tiles, slightly out of focus.

Color palette: Terracotta, warm cream, deep teal, warm gold accents.

Mood: Lively, social, sophisticated-but-approachable, celebratory, with emphasis on vibrant, fresh, celebratory.

Quality: Photorealistic, high detail, professional editorial food photography.
```

---

## Negative Prompt

Always appended. Combines the global brand avoid list with per-brief specifics.

```text
text, lettering, words, logos, watermarks, brand names, signage with readable text, distorted hands, extra fingers, stock photography aesthetic, oversaturated colors, heavy filters, sterile lighting, generic restaurant interior, AI-generated artifacts, plastic-looking food, {brand_avoid_global}, {brief_avoid_specific}
```

---

## Lighting & Time-of-Day Slots

```javascript
const lightingByTime = {
  morning:     "Bright clean morning light, cool tones, fresh and crisp atmosphere",
  midday:      "Bright natural daylight, soft diffused, slight overcast quality",
  golden_hour: "Soft golden hour light from the side, warm afternoon glow, long soft shadows",
  blue_hour:   "Twilight blue hour ambiance, twinkling string lights, magic-hour glow",
  night_warm:  "Warm interior lighting, candles and edison bulbs, intimate evening atmosphere"
};
```

---

## Variation Strategy

Four parallel generations per brief. Don't run the same prompt 4 times — outputs will be near-duplicates. Vary one slot per variation so the user sees genuinely different options.

```javascript
const variations = [
  { label: "Baseline",          prompt: basePrompt },
  { label: "Different angle",   prompt: basePrompt.replace(angle, alternateAngle) },
  { label: "Different lighting",prompt: basePrompt.replace(lighting, alternateLighting) },
  { label: "Editorial push",    prompt: basePrompt + " styled like a New York Times Cooking editorial spread" }
];
```

---

## Reference Image Handling (Gemini multimodal)

Pass references with intent labels so the model knows what to extract from each:

```typescript
const parts = [
  { text: composedPrompt },
  { text: "Reference for lighting and color mood:" },
  { inlineData: lightingRef },
  { text: "Reference for composition and styling:" },
  { inlineData: compositionRef },
  { text: "Do not copy these images directly — use only as style and mood reference." },
  { text: `Negative prompt: ${negative}` }
];
```

---

## Refinement Loop

After the initial 4 options, the user picks one and refines. Five refinement modes:

```javascript
async function refine(originalBrief, chosenImage, refinementType, customText) {
  switch (refinementType) {
    case "more_like_this":
      return generate({
        ...originalBrief,
        reference_asset_ids: [...originalBrief.reference_asset_ids, chosenImage.id]
      });

    case "different_angle":
      return generate({
        ...originalBrief,
        composition_override: "shot from a different angle than the previous attempt"
      });

    case "different_lighting":
      return generate({
        ...originalBrief,
        lighting_override: "alternate lighting time-of-day"
      });

    case "more_vibrant":
      return generate({
        ...originalBrief,
        mood_amplification: "amplified vibrancy and saturation"
      });

    case "custom":
      return generate({
        ...originalBrief,
        custom_addition: customText
      });
  }
}
```

---

## Edge Function Architecture

```
Lovable frontend
  ↓ POST /generate-creative
  ↓ payload: { brief, brand_context_id, references }

Supabase Edge Function: generate-creative
  ↓ load brand context from DB
  ↓ compose prompt from 4 layers
  ↓ build 4 variation prompts
  ↓ call Gemini API × 4 in parallel
  ↓ wait for all responses (Promise.all)
  ↓ save outputs to Supabase Storage
  ↓ insert generation_runs row
  ↓ insert 4 creative_outputs rows
  ↓ return { generation_run_id, outputs: [...] }

Lovable frontend
  ← displays 4 options
  ← user selects → refines → composites with brand layer → saves
```

---

## Database Schema

```sql
-- Stores every generation request and its result
create table generation_runs (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references profiles(id),
  brief_id uuid references briefs(id),
  composed_prompt text not null,
  negative_prompt text not null,
  brief_snapshot jsonb not null,             -- frozen brief at time of run
  brand_context_snapshot jsonb not null,     -- frozen brand context at time of run
  reference_asset_ids uuid[] default '{}',
  model text not null,                       -- 'gemini-2.5-flash-image' etc
  model_params jsonb not null,               -- temperature, etc
  variation_strategy jsonb,                  -- which slots were varied per output
  duration_ms integer,
  cost_usd numeric(10,4),
  created_at timestamptz default now()
);

-- Each generated image is one row
create table creative_outputs (
  id uuid primary key default gen_random_uuid(),
  generation_run_id uuid references generation_runs(id),
  user_id uuid references profiles(id),
  variation_label text,                      -- 'Baseline' | 'Different angle' | etc
  rendered_url text not null,                -- Supabase Storage URL
  composited_url text,                       -- after logo/text overlay
  status text default 'draft',               -- draft, selected, refined, final, archived
  parent_output_id uuid references creative_outputs(id),  -- if refined from another
  template_id uuid references templates(id),              -- if composited via template
  composite_field_values jsonb,              -- text overlay values used
  created_at timestamptz default now()
);
```

Snapshot the brand context inline in `generation_runs` so old generations remain reproducible even when brand settings change.

---

## Post-Generation Composite Step

AI generates the visual base. Brand-locked elements are composited on top using a separate template engine (Placid recommended). This keeps logos, fonts, and text overlays brand-perfect.

```
AI image (base)
  + logo overlay (real PNG, exact placement)
  + headline (real font, exact hex color)
  + body / CTA (structured text fields)
  + required disclaimers (if any)
  = final composited output
```

The composite step is a separate Edge Function (`composite-creative`) that takes the chosen AI output and a template ID, then calls Placid (or canvas API) to overlay locked brand elements.

---

## Implementation Notes

1. **Always save the composed prompt.** Your team will say "I loved last week's margarita shot — make another like it." Without prompt history, you're guessing.

2. **Always snapshot brand context.** Brand voice doc edits 6 months from now shouldn't break the ability to reproduce an old output.

3. **Plan ~10 days of prompt tuning** after the initial build. Slot templates need iteration based on which outputs your team accepts vs. rejects in real use.

4. **Cost expectations.** Gemini 2.5 Flash Image is ~$0.039/image. Four parallel generations ≈ $0.16/brief. Iterating 3–4 times ≈ $0.50/finished asset. Manageable for internal use.

5. **Latency expectations.** Each generation takes 5–15s. Run 4 in parallel — total wait is whichever is slowest, ~15s.

6. **Rate limits.** Gemini has per-minute caps. Build retry-with-backoff into the Edge Function.

7. **Logos are never AI-generated.** Logo overlay always happens in the post-generation composite step.

8. **Text in images.** Avoid generating text in the AI step. Render text as overlay in the composite step using real fonts.

9. **Reference asset cap.** More than 5 reference images creates prompt confusion. Cap at 5.

10. **Variation strategy is core to UX.** Showing 4 near-duplicate outputs feels broken. Showing 4 distinctly different options feels like creative direction.

---

## Quick Reference: Field-to-Slot Map

| Brief Field            | Goes Into Prompt Slot            |
|------------------------|----------------------------------|
| channel                | composition_for_format           |
| goal                   | (context only, not in prompt)    |
| subject                | subject_description              |
| mood                   | brief_mood                       |
| time_of_day            | time_of_day_lighting             |
| text_overlay_planned   | text_overlay_clause              |
| required_props         | required_props_clause            |
| reference_asset_ids    | multimodal reference parts       |
| avoid_specific         | brief_avoid_specific (negative)  |

| Brand Context Field    | Goes Into Prompt Slot            |
|------------------------|----------------------------------|
| brand_name             | brand_name                       |
| photography_style      | photography_style                |
| color_palette          | color_palette                    |
| settings_description   | settings_short / settings_full   |
| mood_baseline          | mood_baseline                    |
| avoid_global           | brand_avoid_global (negative)    |
