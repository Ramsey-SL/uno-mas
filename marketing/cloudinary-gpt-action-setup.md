# Custom GPT Action — Cloudinary Library Search

> ⚠️ **STATUS (2026-06-17): NOT usable in the current ChatGPT GPT builder.** Newer ChatGPT replaced
> the classic "Actions" (paste-OpenAPI-schema) editor with a catalog-only **Apps & Connectors**
> model, and Cloudinary isn't in the catalog — so this Action can't be added. Kept for reference in
> case custom Actions/Apps-SDK return. **Fallback for DAM lookups:** ask Claude (live Cloudinary MCP
> access) or use Cloudinary's Media Library search directly. The GPT still has brand pack + logos +
> live GitHub, which is the core value.

Lets the "Uno Más Art Director" GPT search your full Cloudinary library — the **`uno-mas`** and
**`mezzanine`** namespaces (all subfolders). Returns links/metadata — it does NOT feed generation;
you still attach a returned image as a reference if you want to generate from it.

- **Cloud name:** `drxrfyq9i`
- **Endpoint:** Cloudinary Admin Search API — `POST /resources/search` (Basic auth)
- **Scope guard (verified to cover all 154 assets):**
  `(asset_folder:uno-mas/* OR public_id:uno-mas/* OR asset_folder:mezzanine/* OR public_id:mezzanine/*)`

> Why the OR: some assets store the folder in `asset_folder` (dynamic folders), others have an empty
> `asset_folder` with the path in `public_id` (e.g. the website/buildout set). Matching both fields
> across both namespaces is the only complete scope.

---

## Step 1 — Get Cloudinary credentials
Cloudinary Console → **Settings → API Keys** (or the Dashboard). You need the **API Key** and
**API Secret** for cloud `drxrfyq9i`. Best practice: create a **dedicated key** you can revoke later.

## Step 2 — Build the Basic-auth token (run locally, do NOT paste the secret into chat)
```bash
printf '%s' 'YOUR_API_KEY:YOUR_API_SECRET' | base64
```
Copy the output (you'll paste it as the auth value in Step 4).

## Step 3 — Add the Action to the GPT
GPT → **Configure → Actions → Create new action** → paste the schema below into **Schema**.

```yaml
openapi: 3.1.0
info:
  title: Uno Más Cloudinary Library Search
  description: Search the Uno Más + Mezzanine asset library in Cloudinary.
  version: 1.1.0
servers:
  - url: https://api.cloudinary.com/v1_1/drxrfyq9i
paths:
  /resources/search:
    post:
      operationId: searchLibrary
      summary: Search the Uno Más / Mezzanine asset library by keyword.
      description: >
        Search the Cloudinary library scoped to the brand namespaces. The expression MUST always
        wrap the brand scope in parentheses and AND the user's keywords. Required scope:
        "(asset_folder:uno-mas/* OR public_id:uno-mas/* OR asset_folder:mezzanine/* OR public_id:mezzanine/*)".
        Example: "(asset_folder:uno-mas/* OR public_id:uno-mas/* OR asset_folder:mezzanine/* OR public_id:mezzanine/*) AND (taco OR carne)".
        Return each result's display_name and secure_url; offer to attach one as a reference for generation.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [expression]
              properties:
                expression:
                  type: string
                  description: >
                    Cloudinary search expression. ALWAYS include the brand scope
                    "(asset_folder:uno-mas/* OR public_id:uno-mas/* OR asset_folder:mezzanine/* OR public_id:mezzanine/*)"
                    then AND the keywords.
                max_results:
                  type: integer
                  default: 20
      responses:
        '200':
          description: Search results
          content:
            application/json:
              schema:
                type: object
                properties:
                  total_count: { type: integer }
                  resources:
                    type: array
                    items:
                      type: object
                      properties:
                        public_id: { type: string }
                        secure_url: { type: string }
                        display_name: { type: string }
                        asset_folder: { type: string }
                        width: { type: integer }
                        height: { type: integer }
```

## Step 4 — Authentication
In the Action's **Authentication** panel:
- Type: **API Key**
- Auth Type: **Custom**
- Custom Header Name: `Authorization`
- API Key (value): `Basic <paste the base64 string from Step 2>`  ← include the word `Basic ` and a space

(If your builder version offers "Basic" directly, paste just the base64 string.)

## Step 5 — Add this to the GPT Instructions
```
When the user wants an existing photo from the library, call searchLibrary. ALWAYS include the
brand scope "(asset_folder:uno-mas/* OR public_id:uno-mas/* OR asset_folder:mezzanine/* OR
public_id:mezzanine/*)" and AND the keywords. Keep Uno Más and Mezzanine results clearly separated.
Return display_name + a clickable secure_url for each hit, and offer to attach one as a reference.
These are real brand assets — never redraw or fake them.
```

## Notes
- Scope verified 2026-06-17: the OR expression returns all 154 library assets (uno-mas = 100, mezzanine = 14, plus the website/buildout set matched via public_id).
- Keyword matching depends on filenames/display-names/tags; if results are thin, broaden keywords or add tags in Cloudinary.
- The API secret grants broad account access — keep it ONLY in the ChatGPT Action auth field, never in the schema/repo/chat. This Action is read/search only (no upload/edit/delete).
