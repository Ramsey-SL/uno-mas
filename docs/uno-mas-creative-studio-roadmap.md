# Uno Más Creative Studio — Project Notes & Future Roadmap

_Last updated: 2026-04-29_

## Product Vision

Uno Más Creative Studio is an internal creative production tool for Uno Más Tacos & Tequila. The goal is to help the team create on-brand social posts, ads, flyers, campaign assets, and promotional creative using approved brand guidelines, approved assets, inspiration boards, and AI-assisted workflows.

The system should function like an internal brand-safe creative engine:

```text
Campaign details
+ Brand guidelines
+ Approved assets
+ Style board
+ Inspiration board
+ Template/framework
= On-brand creative concepts
```

## Current MVP Scope

### Core Workflow

```text
Create campaign
→ Select content format/template
→ Enter campaign details, offer, platform, audience, and required text
→ Select style board
→ Select approved assets
→ Generate 3–5 visual creative concepts
→ Select concept to refine
→ Annotate text/layout areas
→ Apply prompt-based edits to output_json
→ Export final creative
→ Save winning design as reusable framework
```

### MVP Features

- Supabase authentication
- Admin/editor user roles
- Admin role badge in sidebar
- Dashboard as default post-login page
- Brand Center
- Brand guideline storage via `brand_guidelines`
- Approved asset library
- Direct local asset upload
- Asset submission workflow
- Admin asset review workflow
- Approved assets only in creative builder
- AI-assisted asset tagging/categorization
- Campaign builder
- Style boards
- Inspiration boards
- Visual generated concept previews
- Refinement editor
- Annotation-based text/layout editing
- Save annotations
- Apply annotation changes to structured `output_json`
- Save final concepts as reusable frameworks

## MVP Annotation Editing Requirements

Annotation-based editing is included in the MVP.

Users should be able to:

1. Open a generated concept in the Refinement Editor.
2. Turn on annotation mode.
3. Draw a rectangle over part of the design preview.
4. Add a prompt/comment for the selected area.
5. Save the annotation.
6. Apply the change.
7. Update only the relevant section of `creative_outputs.output_json`.
8. Re-render the visual design preview.
9. Mark the annotation as resolved.

### Supported MVP Annotation Edits

- Headline edits
- Subheadline edits
- CTA edits
- Caption edits
- Text size
- Text placement
- Text alignment
- Logo placement
- Image crop
- Approved asset swap
- Background treatment
- Color treatment
- Layout direction
- Spacing
- Element hierarchy

### MVP Annotation Limitations

The MVP should not perform true pixel-level image editing. Instead, all edits should modify structured design data.

Do not include in MVP:

- Inpainting
- Generative fill
- Object removal
- Object replacement inside uploaded images
- True photo retouching
- AI-generated replacement backgrounds

For image-related prompts, the MVP should handle edits by:

- Swapping to another approved asset
- Adjusting crop values
- Adjusting overlay styles
- Adjusting layout values
- Adjusting background treatment
- Recommending a different approved asset

## Asset System Notes

### Asset Storage

Files should be stored in Supabase Storage for the MVP.

Recommended buckets:

```text
asset-submissions
approved-assets
inspiration-items
```

### Asset Metadata

The database should store asset metadata separately from the file itself.

Important metadata fields:

- name
- type
- url
- tags
- status
- category
- use_cases
- orientation
- file_name
- file_size
- mime_type
- width
- height
- duration_seconds
- storage_bucket
- storage_path
- thumbnail_url
- campaign
- source
- usage_notes
- approved_by
- approved_at
- archived_at

### Asset Approval Workflow

```text
User uploads asset
→ File stored in asset-submissions bucket
→ Metadata saved to asset_submissions
→ Status = pending_review
→ Admin reviews
→ Admin approves or rejects
→ Approved assets are copied/registered in assets table
→ Approved assets become available in creative builder
```

### AI-Assisted Asset Tagging

When users upload assets, the system should suggest editable metadata:

- asset_type
- category
- tags
- use_cases
- orientation
- short description
- usage_notes

Suggestions are drafts only. Users must be able to edit before saving.

### Controlled Categories

```text
tacos
margaritas
cocktails
chips_salsa
interior
patio
team
events
nightlife
brand
menu
general_vibe
texture
background
```

### Controlled Use Cases

```text
instagram_post
instagram_story
reel
ad
flyer
menu
website
email
background
logo_lockup
```

### Controlled Orientations

```text
square
vertical
horizontal
wide
transparent
```

## Inspiration Boards

Inspiration boards should function like Pinterest-style boards for creative direction.

They are used to inform the look, layout, photography direction, typography feel, composition, and creative mood of generated concepts.

### Inspiration Board Examples

- Street Taco Grit
- Premium Tequila Lounge
- Patio Happy Hour
- Bold Cantina Energy
- Cinco de Mayo
- Late Night Margarita Energy
- Modern Mexican Minimal
- Family Fiesta
- Spokane Local Night Out

### Inspiration Board Items

Each board may include:

- screenshots
- photos
- ads
- menus
- social posts
- textures
- typography inspiration
- color references
- layout inspiration
- lighting references
- composition examples

### Use in Creative Generation

The system should not directly copy inspiration images. It should extract directional guidance such as:

- high-contrast food photography
- bold condensed headline hierarchy
- textured overlays
- warm cantina lighting
- diagonal composition
- premium cocktail mood
- patio lifestyle energy

The generated concepts should explain:

- which inspiration cues were used
- how they were adapted to Uno Más
- why the result remains on-brand

## Brand Context System

Brand context should come from the Uno Más GitHub repo and/or records imported into Supabase `brand_guidelines`.

Important brand context categories:

- colors
- typography
- logo rules
- voice
- tone
- photography
- design rules
- social copy
- promotions
- menu context
- brand history
- content examples

Creative generation should query active `brand_guidelines` and include the relevant rules in the AI prompt.

The tool should not invent brand colors, logo rules, menu context, or tone if brand guidelines exist.

## Future Roadmap / Later Phase Features

These are intentionally not required for the MVP, but should be preserved for later planning.

### Advanced Creative Editing

- True AI image editing
- Region-based inpainting
- Generative fill
- Object removal
- Object replacement
- Background replacement
- AI image variations
- Product/food retouching
- Lighting/style transfer on uploaded photos
- Automatic background removal
- Image upscaling
- Image cleanup/restoration

### Advanced Asset Integrations

- Google Drive asset import
- Google Drive folder sync
- Canva asset import
- Canva Brand Kit sync
- Canva template import/reference
- Push final concepts into Canva for editing
- Figma import/export
- Dropbox/Box import

### Advanced Export Workflows

- Canva export/edit integration
- Figma export/edit integration
- Multi-size campaign resizing
- Automated Meta ad creative package generation
- Campaign set generation: post, story, reel cover, ad, flyer
- Export to Google Drive folder
- Export to social media scheduling platform
- Export with caption/copy package

### Advanced Brand Governance

- Brand compliance scoring
- Off-brand warning system
- Approval workflow for generated creative
- Version history for concepts
- Commenting/review threads
- Creative approval status
- Admin-managed locked brand rules

### Advanced AI Strategy

- Campaign performance feedback loop
- Learn from top-performing past posts
- Style recommendation based on campaign goal
- Asset recommendation based on campaign type
- Audience-specific copy variations
- A/B test creative generation
- Seasonal campaign playbooks

## Implementation Notes

### MVP Data Tables

Current/expected core tables:

- profiles
- user_roles
- campaigns
- style_boards
- brand_guidelines
- assets
- asset_submissions
- templates
- creative_outputs
- frameworks
- inspiration_boards
- inspiration_items
- design_annotations

### MVP Principle

The MVP should prioritize structured, reliable creative generation over full pixel-level editing.

The best first version is:

```text
Brand-safe data
+ Approved assets
+ Structured templates
+ Visual previews
+ Annotation-based output_json editing
```

This creates a controlled internal creative workflow while leaving room for advanced AI image editing later.
