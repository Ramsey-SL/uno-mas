# Custom GPT Action — Cloudinary Approved-Asset Search

Lets the "Uno Más Art Director" GPT search your Cloudinary DAM and return **approved** assets only
(scoped to `uno-mas/approved-assets/`). It returns links/metadata — it does NOT feed generation;
you still attach a returned image as a reference if you want to generate from it.

- **Cloud name:** `drxrfyq9i`
- **Endpoint:** Cloudinary Admin Search API — `POST /resources/search` (Basic auth)
- **Scope guard:** every search must include `public_id:uno-mas/approved-assets/*`

---

## Step 1 — Get Cloudinary credentials
Cloudinary Console → **Settings → API Keys** (or the Dashboard). You need the **API Key** and
**API Secret** for cloud `drxrfyq9i`. Best practice: create a **dedicated key** for this so you can
revoke it later without breaking other things.

## Step 2 — Build the Basic-auth token (run locally, do NOT paste the secret into chat)
```bash
printf '%s' 'YOUR_API_KEY:YOUR_API_SECRET' | base64
```
Copy the output string (you'll paste it as the auth value in Step 4).

## Step 3 — Add the Action to the GPT
GPT → **Configure → Actions → Create new action** → paste the schema below into **Schema**.

```yaml
openapi: 3.1.0
info:
  title: Uno Más Cloudinary Approved-Asset Search
  description: Search the Uno Más approved asset library in Cloudinary.
  version: 1.0.0
servers:
  - url: https://api.cloudinary.com/v1_1/drxrfyq9i
paths:
  /resources/search:
    post:
      operationId: searchApprovedAssets
      summary: Search approved Uno Más assets by keyword.
      description: >
        Search the Cloudinary library for APPROVED assets only. The expression MUST always
        include "public_id:uno-mas/approved-assets/*" combined with the user's keywords.
        Example: "public_id:uno-mas/approved-assets/* AND (taco OR carne)". Return each
        result's display_name and secure_url; offer to attach one as a reference for generation.
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
                    Cloudinary search expression. ALWAYS start with
                    "public_id:uno-mas/approved-assets/*" then AND the keywords.
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
                  total_count:
                    type: integer
                  resources:
                    type: array
                    items:
                      type: object
                      properties:
                        public_id: { type: string }
                        secure_url: { type: string }
                        display_name: { type: string }
                        width: { type: integer }
                        height: { type: integer }
```

## Step 4 — Authentication
In the Action's **Authentication** panel:
- Type: **API Key**
- Auth Type: **Custom**
- Custom Header Name: `Authorization`
- API Key (value): `Basic <paste the base64 string from Step 2>`  ← include the word `Basic ` and a space

(If your builder version offers "Basic" directly, you can use that and paste just the base64 string.)

## Step 5 — Add this to the GPT Instructions
```
When the user asks for an existing/approved photo, call searchApprovedAssets. ALWAYS scope the
expression with "public_id:uno-mas/approved-assets/*". Never search outside approved-assets.
Return display_name + a clickable secure_url for each hit, and offer to attach one as a reference
for a new generation. These are real approved assets — never redraw or fake them.
```

## Security notes
- The API secret grants broad account access. Keep it ONLY in the ChatGPT Action auth field — never
  in the schema, the repo, or chat. Use a dedicated key you can rotate/revoke.
- This Action is **read/search**. It does not upload, edit, or delete.
