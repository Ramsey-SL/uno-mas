# Brand Guidelines Import — Uno Más Creative Studio

**Generated:** 2026-04-30
**Records:** 39 (all `content` fields ≤ 2,000 chars to satisfy Creative Studio validation)

## What this fixes

The Creative Studio "Generate concepts" step was failing with this error:

```
"String must contain at most 2000 character(s)"
"path": ["brand_guidelines", 0, "content"]
```

The cause: brand intelligence MD files were imported as full documents into single `brand_guidelines` records. Each was thousands of characters long.

These files split that content into 39 focused records, each under 2,000 chars and tagged by category, so the AI can pull exactly the rules it needs per generation.

## Files in this bundle

| File | When to use |
|---|---|
| `brand_guidelines_import.json` | Programmatic import via your Supabase client. Cleanest format. |
| `brand_guidelines_import.csv` | Drag-and-drop import via Supabase Studio → Table Editor → Insert → Import data from CSV. |
| `brand_guidelines_import.sql` | Direct SQL execution in Supabase SQL Editor. Use if you want full control. |
| `build_brand_guidelines.py` | Source script. Re-run anytime you update the brand MDs. |

## Suggested table schema

If your `brand_guidelines` table doesn't already match, here's a reasonable shape:

```sql
create table brand_guidelines (
  id          text primary key,
  name        text not null,
  category    text not null,
  content     text not null check (length(content) <= 2000),
  tags        text[] default '{}',
  brand       text default 'uno-mas',
  priority    text default 'medium',
  is_active   boolean default true,
  created_at  timestamptz default now(),
  updated_at  timestamptz default now()
);

create index brand_guidelines_brand_active_idx on brand_guidelines (brand, is_active);
create index brand_guidelines_category_idx on brand_guidelines (category);
```

If your existing schema uses different column names, update either the import file or the table to match.

## Categories included

| Category | Records | Purpose |
|---|---|---|
| `business` | 2 | Identity, concept, team, contact |
| `messaging` | 2 | One-liners, tagline, mission |
| `audience` | 6 | Personas, occasions, JTBD, switching dynamics, language, anti-persona |
| `voice` | 7 | Personality, traits, persona, tone-by-context, ALWAYS, NEVER, vocabulary swaps, Mezzanine sub-brand |
| `visual` | 7 | Uno Más colors/typography/logo, Mezzanine colors/typography/logo, brand separation rules |
| `positioning` | 4 | Position summary, three venues, food & beverage, events/loyalty differentiators |
| `competitive` | 2 | Direct competitors, indirect alternatives + objection handling |
| `digital` | 2 | Ecosystem (web, social, reservations, marketing stack), search terms |
| `proof` | 4 | Performance metrics, dinner validation, testimonials, what we're known for |
| `goals` | 2 | Conversion goals, current business focus |
| `financial` | 1 | Revenue, growth levers, marketing implications |

**Total: 39 records, max content length 1,521 chars.**

## Recommended import steps

1. **Back up your current `brand_guidelines` table** (Supabase Studio → Table Editor → Export to CSV, or run a `pg_dump`).
2. **Clear the existing oversized rows** — delete the records currently triggering validation errors, or clear the table if you're starting fresh:
   ```sql
   DELETE FROM brand_guidelines WHERE brand = 'uno-mas';
   ```
3. **Import this bundle** using your preferred file from the table above.
4. **Verify in the app** — refresh the Creative Studio Brand Center, confirm all 39 records appear and `is_active = true`.
5. **Re-run "Generate concepts"** — should now pass validation.

## How the AI will use these records

In your Creative Studio app's prompt assembly logic, query records by:
- `brand = 'uno-mas'` and `is_active = true`
- Filter by `category` based on the generation type:
  - Generating ad copy → pull `voice`, `messaging`, `audience`, `goals`, `proof`
  - Generating menu visuals → pull `visual`, `business`, `voice`
  - Generating Mezzanine content → filter `tags @> ARRAY['mezzanine']` and use Mezzanine-specific records
- Concatenate the relevant `content` fields into the AI prompt

This is the structured-rules approach the roadmap calls for: discrete brand rules the AI references, rather than monolithic documents.

## Next time you update brand intelligence

1. Update the source MD in `brand-intelligence-center/`
2. Re-run the build script (`python3 build_brand_guidelines.py`)
3. Re-import the changed records (or upsert by id)
