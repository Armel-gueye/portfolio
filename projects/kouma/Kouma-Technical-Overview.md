# Kouma — Technical Overview & Architecture

> **Public Portfolio Specification & Engineering Summary**  
> *Author / Full-Stack & AI Systems Engineer*  
> *Application Name: Kouma* | *Stack: TypeScript, React 18, Node.js/Express, Supabase (pgvector), Google Gemini, Cohere, Docker*

---

## 1. Project Overview & Purpose

**Kouma** is an enterprise-grade, privacy-focused conversational AI SaaS platform designed to enable businesses to create, configure, train, and deploy customized, context-aware AI chatbots to their websites within minutes.

### The Problem
Small to medium enterprises and digital teams frequently struggle with high customer support loads, missed lead-generation opportunities outside business hours, and cumbersome, hallucination-prone generic chatbot plugins. Traditional bots either require extensive NLP developer setup or lack domain grounding on proprietary company documentation.

### The Solution
Kouma bridges this gap with an end-to-end self-service solution:
1. **Zero-Code Onboarding & Visual Customization**: Businesses customize chat avatars, color palettes, fonts, positioning, launcher icons, and brand voice.
2. **Deterministic Retrieval-Augmented Generation (RAG)**: Assistants are grounded strictly in company documentation (PDF manuals, internal guides, FAQ documents, and live website scrapes) using semantic vector search.
3. **Autonomous Lead Capture**: Chatbots proactively qualify visitors during natural dialogue and autonomously trigger background lead-saving tool calls (function calling) whenever contact details are shared.
4. **Embeddable Shadow DOM Widget**: A lightweight, script tag integration that mounts completely isolated within any CMS (WordPress, Shopify, Webflow) or custom web stack without CSS leakage.
5. **Enterprise-Grade Security & GDPR Compliance**: Comprehensive session binding, anti-SSRF protections, multi-tier rate limiting, brute-force lockouts, and one-click cascading data erasure.

---

## 2. Core Functional Features

| Feature Module | Description & Capabilities |
| :--- | :--- |
| **Bot Studio & Customizer** | Real-time interactive preview for tweaking bot names, welcome messages, support emails, system preambles, and conversational tones (*professional, friendly, concise, empathetic*). |
| **Widget Theming Engine** | Granular control over primary colors, message bubble backgrounds, typography, border radius (shapes), widget placement (bottom-right vs. bottom-left), and custom launcher icons. |
| **Document Ingestion Engine** | Client-side chunking and extraction of multi-page PDF files via `pdfjs-dist`, server-side safe website scraping via Cheerio, and arbitrary manual knowledge base entries. |
| **Dual AI Provider Architecture** | First-class support for both **Cohere** (`command-r-plus`, `embed-multilingual-v3.0`) and **Google Gemini** (`gemini-3.1-flash-lite`, `gemini-embedding-2-preview`). Users can run on global platform keys or provide BYOK (Bring-Your-Own-Key) credentials. |
| **Autonomous Function Calling (Leads)** | Real-time tool execution (`sauvegarder_lead`) allowing the LLM to autonomously detect visitor contact info (name, email, phone, company) and trigger lead capture without interrupting conversational flow. |
| **Instant Email Dispatch** | Automated transactional email notifications dispatched via Resend to the business owner whenever a new prospect is captured. |
| **Conversation History & Inbox** | Full dialogue logging and inbox inspection interface displaying multi-turn visitor conversations, timestamps, and captured prospect details. |
| **Data Privacy & GDPR Suite** | Built-in GDPR cascade deletion endpoint (`/api/auth/delete-account`), opt-in consent logging, privacy policies, terms of service, and 30-minute inactivity auto-logout. |

---

## 3. Role & Engineering Contributions

As the primary engineer responsible for architecting and developing Kouma, key contributions include:

- **End-to-End System Design**: Conceived and implemented both the React single-page dashboard and the hardened Express backend, ensuring zero-trust credential isolation.
- **RAG Pipeline Implementation**: Built the client-side document processing pipeline (PDF extraction, text normalization, sliding-window chunking) and backend cosine similarity search using Postgres `pgvector`.
- **LLM Streaming & Function Calling Engine**: Designed streaming endpoints for both Cohere and Gemini using Server-Sent Events (SSE) and chunked transfer encoding, implementing server-side JSON tool execution for lead capture.
- **Security Engineering & Session Hardening**: Authored a custom stateful security engine (`SessionSecurityEngine`) with cryptographic session binding (IP + User-Agent fingerprinting), brute-force account lockouts, honeypots, and strict SSRF defenses.
- **Shadow DOM Widget Construction**: Developed a dependency-free, cross-browser embed script (`widget.js`) with isolated Shadow DOM styling, postMessage synchronization, and responsive iframe viewports.
- **DevOps & Production Readiness**: Authored containerization recipes (`Dockerfile`, `docker-compose.yml`), Sentry observability pipelines, and automated build scripts.

---

## 4. High-Level System Architecture

```
                                  +---------------------------------------+
                                  |         External Website              |
                                  |    (WordPress / Shopify / Webflow)    |
                                  +---------------------------------------+
                                                      |
                                          <script src="widget.js">
                                                      |
                                                      v
                                        +----------------------------+
                                        |   Kouma Shadow DOM Host    |
                                        |   (Isolated CSS / Sandbox) |
                                        +----------------------------+
                                                      |
                                            postMessage / Iframe
                                                      |
                                                      v
+---------------------------------------------------------------------------------------------------------+
|                                           KOUMA PLATFORM                                                |
|                                                                                                         |
|   +-----------------------------------+             +-----------------------------------------------+   |
|   |         React 18 SPA              |             |            Node.js / Express Server           |   |
|   |   (Vite, Tailwind, Motion,        |             |   - Session Security Engine (IP/UA Hash)      |   |
|   |    Zod, Sonner, Sentry React)     |             |   - Multi-Tier Rate Limiters                  |   |
|   +-----------------------------------+             |   - Anti-SSRF Scraping Service                |   |
|                     |                               |   - Server-Side System Prompt Assembly        |   |
|                     | HTTPS (REST / SSE)            |   - Autonomous Tool Declarations              |   |
|                     +-----------------------------> |   - Sentry Global Error Interceptors          |   |
|                                                     +-----------------------------------------------+   |
|                                                                     |                   |               |
|                                           +-------------------------+                   |               |
|                                           |                                             |               |
+-------------------------------------------|---------------------------------------------|---------------+
                                            v                                             v
                         +--------------------------------------+      +----------------------------------+
                         |      External AI Services            |      |      Supabase / PostgreSQL       |
                         |  - Cohere (command-r-plus / embed)   |      |  - Auth (JWT / User Identities)  |
                         |  - Google Gemini (Flash / Embed)     |      |  - pgvector (Cosine Sim RPCs)    |
                         |  - Resend (Transactional Emails)     |      |  - Tables: bots, leads, messages |
                         +--------------------------------------+      +----------------------------------+
```

---

## 5. Technology Stack

### Frontend Core
- **Language & Runtime**: TypeScript, React 18, Vite.
- **Styling & Design System**: Tailwind CSS, CSS Custom Properties for dynamic branding, Lucide React icons.
- **Motion & Interactions**: `motion/react` (Framer Motion) for route transitions and interactive UI panels.
- **Notifications & Modals**: Sonner (toast notifications), Radix UI primitives.
- **Validation & Schema**: Zod schemas for client-side form validations.
- **Document Processing**: `pdfjs-dist` (client-side PDF page rendering and text layer extraction).
- **Observability**: `@sentry/react` for frontend error capture and performance tracking.

### Backend Core
- **Runtime**: Node.js (v20+ LTS), Express.js.
- **Build System**: `esbuild` bundled CommonJS for optimized container startup (`dist/server.cjs`), `tsx` for live local development.
- **Data Proxy & Validation**: `http-proxy-middleware` with response interception, Zod for schema enforcement, `xss` for payload sanitization.
- **Web Scraping & DOM Processing**: `cheerio` for HTML parsing, custom DNS resolving for SSRF filtering.
- **Email Service**: `resend` for automated email dispatch.
- **Observability**: `@sentry/node` for server exception monitoring.

### Database & Vector Engine
- **Primary Database**: PostgreSQL hosted on Supabase.
- **Vector Storage**: `pgvector` extension for storing and indexing high-dimensional vector embeddings.
- **Authentication**: Supabase Auth (JWT tokens, password recovery, session tokens).

---

## 6. RAG Architecture & Document Processing Workflow

Kouma implements a multi-stage, deterministic Retrieval-Augmented Generation pipeline designed to eliminate hallucinations by restricting responses to indexed corporate knowledge.

```
+----------------------------------------------------------------------------------------------------+
| 1. INGESTION PHASE                                                                                 |
|                                                                                                    |
|   [PDF Files]        --> Client-side `pdfUtils.ts` (PDF.js text layer extraction & normalization)  |
|   [Web URL Scrape]   --> Server-side `/api/scrape` (Cheerio content sanitization & SSRF guard)     |
|   [Raw Knowledge]    --> Direct text input via Studio dashboard                                    |
+----------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
+----------------------------------------------------------------------------------------------------+
| 2. CHUNKING & PRE-PROCESSING                                                                       |
|                                                                                                    |
|   - Algorithm: Recursive character / sentence sliding window (`ragUtils.ts`)                       |
|   - Default Parameters: Chunk size = 1,000 characters; Overlap = 200 characters; Min length = 100  |
|   - Metadata Binding: Document ID, Bot ID, Source Name, Page Number, Chunk Index                   |
+----------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
+----------------------------------------------------------------------------------------------------+
| 3. EMBEDDING & VECTOR STORAGE                                                                      |
|                                                                                                    |
|   - Cohere Pipeline: `embed-multilingual-v3.0` -> 1,024-dimensional float vectors                  |
|   - Gemini Pipeline: `gemini-embedding-2-preview` -> 768-dimensional float vectors                 |
|   - Destination: Supabase `bot_documents` table with `vector(1024)` / `vector(768)` indexes        |
+----------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
+----------------------------------------------------------------------------------------------------+
| 4. REAL-TIME RETRIEVAL & AUGMENTATION (CHAT QUERY)                                                 |
|                                                                                                    |
|   User Query -> Embedding API -> Vector Search RPC (`match_bot_documents[_gemini]`)                |
|   - Match Threshold: 0.2 Cosine Similarity                                                         |
|   - Top-K Match Count: 5 most relevant chunks retrieved                                            |
|   - Server-Side Injection: Formatted into system prompt context before LLM generation              |
+----------------------------------------------------------------------------------------------------+
```

### Key RAG Implementation Details:
- **Clean Ingestion**: Text chunks are scrubbed of surrogate pairs, zero-width spaces, and control characters to prevent vector embedding failures.
- **Server-Side Context Enclosure**: The client never sees raw vector payloads. Matching is executed server-side via Supabase RPCs (`match_bot_documents` for Cohere and `match_bot_documents_gemini` for Gemini), keeping system prompts and corporate IP protected from client-side inspection.

---

## 7. AI & LLM Model Integrations

Kouma leverages a multi-LLM architecture, allowing bot owners to select the AI provider best suited for their budget, latency, and language requirements.

| Provider | Chat Model | Embedding Model | Vector Dim | Features Utilized |
| :--- | :--- | :--- | :--- | :--- |
| **Cohere** | `command-r-plus` / `command-r` | `embed-multilingual-v3.0` | 1024 | Multilingual reasoning, enterprise search input type (`search_query` vs. `search_document`), native tools API. |
| **Google Gemini** | `gemini-3.1-flash-lite` | `gemini-embedding-2-preview` | 768 | Low-latency streaming, `@google/genai` SDK, structured function declarations (`tools` & `functionDeclarations`). |

### Autonomous Tool Calling (Lead Capture)
Both models are configured server-side with a dynamic function declaration:
```json
{
  "name": "sauvegarder_lead",
  "description": "Background tool called to record visitor contact info whenever volunteered during dialogue.",
  "parameters": {
    "email": { "type": "string" },
    "nom": { "type": "string" },
    "telephone": { "type": "string" },
    "entreprise": { "type": "string" }
  }
}
```
When a visitor mentions *"You can reach me at alex@example.com"*, the model produces a tool call event. The server intercepts this event, saves the lead to PostgreSQL, issues a Resend notification to the bot owner, and streams the conversational reply back to the user without interruption.

---

## 8. API Design & Key Endpoints

All custom endpoints reside behind `/api/*` and enforce strict rate limiting, sanitization, and session validation.

### Public & Widget Endpoints
- `POST /api/cohere/chat`: Streams responses from Cohere via chunked transfer encoding; performs server-side RAG document retrieval; handles tool call interceptors.
- `POST /api/gemini/chat`: Streams responses from Google Gemini via Server-Sent Events (SSE); performs server-side RAG retrieval; executes tool declarations.
- `POST /api/leads`: Public endpoint for recording visitor lead submissions.
- `POST /api/notify-lead`: Sends transactional alert email to the site owner via Resend upon lead capture.
- `GET /api/conversations/:id/history`: Retrieves multi-turn conversation logs for a specific session ID.

### Admin & Studio Endpoints (Protected)
- `POST /api/bots`: Creates a new chatbot configuration (protected by `requireAuth` and Zod validation).
- `PUT /api/bots/:id`: Updates chatbot branding, system prompt, or lead collection flags (enforces ownership checks).
- `POST /api/scrape`: Secure website scraping endpoint with SSRF validation.
- `POST /api/cohere/embed` & `POST /api/gemini/embed`: Generates vector embeddings for chunked documents.
- `DELETE /api/auth/delete-account`: GDPR cascade deletion removing all user data, bots, vector documents, leads, and sessions.
- `POST /api/auth/logout-everywhere`: Global session revocation across all active devices.

### Proxied Supabase Gateway
- `/api/supabase/*`: Reverse-proxied route to Supabase Auth and Database using `http-proxy-middleware`. Injects backend `SUPABASE_ANON_KEY` server-side, preventing direct public exposure of sensitive database infrastructure.

---

## 9. Database, Vector Storage & State Management

### Database Schema (PostgreSQL)
1. **`bots`**: Core chatbot entity storing branding colors, layout choices, system prompt, welcome message, collection toggles (`collect_email`, `collect_phone`, etc.), and user ownership.
2. **`bot_documents`**: Text chunks with metadata and vector embeddings (`vector(1024)` / `vector(768)`).
3. **`conversations`**: Dialogue session threads linked to `chatbot_id` and visitor identifiers.
4. **`messages`**: Individual turns (`user` or `assistant`) associated with a conversation.
5. **`leads`**: Qualified contact records (`name`, `email`, `phone`, `company`, `consent_given`, `consent_date`).
6. **`user_sessions`**: Active authentication sessions linked to client IP and User-Agent hashes for zero-trust token hijacking prevention.

### Client-Side State Management
- **React State & Hooks**: Lightweight, modular state management utilizing local React hooks and Context for theme, bot configurations, and active chat dialogues.
- **Inactivity Tracker**: Background window event listener monitoring user actions (mouse, keyboard, touch) with throttled updates, triggering automatic logout after 30 minutes of inactivity.

---

## 10. Embeddable Widget & Third-Party Integration

The public widget is distributed as a single script tag that loads the widget and identifies the configured bot.
```

### Architecture of `widget.js`:
- **Shadow DOM Isolation**: The widget mounts a custom `#kouma-widget-host` element and attaches an isolated Shadow DOM (`attachShadow({ mode: 'closed' })`). This guarantees that host site CSS (e.g., Bootstrap, Tailwind, or WordPress themes) never breaks widget styling.
- **Cross-Origin Security**: Embeds the conversational interface via an iframe pointing to `/embed/:botId`.
- **Bidirectional Communication**: Uses `window.postMessage` with origin checks to communicate state between the iframe and the host (e.g., dynamic resizing, expand/collapse toggles, mobile full-screen expansion).
- **Mobile Adaptive**: Automatically detects viewport widths under 640px and expands into an ergonomic full-screen modal with safe-area padding.

---

## 11. Security, Authentication & Privacy (GDPR)

### 1. Cryptographic Session Binding (`SessionSecurityEngine`)
- Generates a cryptographically random session ID upon login.
- Generates an SHA-256 fingerprint from the client's IP address and User-Agent string.
- Validates the fingerprint on every subsequent API request. If an access token is stolen and used from a different IP or device, access is immediately revoked.

### 2. Multi-Tiered Rate Limiting
Custom rate limiters enforced by route classification:
- **Authentication**: Max 10 req/min per IP.
- **Data Writes**: Max 25 req/min per user.
- **Data Reads**: Max 80 req/min per user.
- **Document Ingestion & Scraping**: Max 10 req/hr per user.
- **Chatbot Queries**: Max 30 req/hr per visitor.
- **Vector Embeddings**: Max 100 req/hr per user.

### 3. Anti-Brute-Force & Account Lockout
- **IP Protection**: 5 consecutive failed login attempts blocks the IP address for 15 minutes.
- **Account Protection**: 10 failed login attempts locks the specific account for 30 minutes and triggers a secure unlock email with a one-time cryptographic token via Resend.

### 4. Server-Side Request Forgery (SSRF) Guard
The `/api/scrape` endpoint resolves target hostnames using Node `dns.promises.lookup` and rejects:
- Loopback addresses (`127.0.0.0/8`, `::1`).
- Private ranges (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`).
- Link-local and cloud metadata addresses (`169.254.169.254`).
- Non-HTTP/HTTPS protocols.

### 5. Input Sanitization & Abuse Filtering
- Recursive payload checks strip HTML tags (`xss` library).
- Automated regex filters flag and block obvious SQL injection patterns and script injections.
- Invisible honeypot inputs (`_hp_catch`, `username_verification`) catch and reject automated spam bots silently.

### 6. Full GDPR Compliance
- Explicit visitor consent tracking for lead submissions.
- Cascade deletion endpoint (`DELETE /api/auth/delete-account`) that destroys the Supabase Auth user, all created bots, stored vector chunks, leads, chat transcripts, and active sessions, followed by a formal email confirmation.

---

## 12. Monitoring, Error Handling & Reliability

- **Frontend Sentry**: Captures client exceptions, failed network requests, and unhandled promise rejections with performance sampling and session replay.
- **Backend Sentry**: Configured via `@sentry/node` with custom Express error-handling middleware.
- **Sanitized Errors**: The API catches low-level exceptions, logs full stack traces server-side, and returns sanitized, user-friendly error messages with unique request correlation IDs.

---

## 13. Deployment, Containerization & Infrastructure

- **Container Engine**: Docker multi-stage build (`Dockerfile`):
  - *Build Stage*: Node 20 alpine, compiles frontend assets with Vite and bundles server logic with `esbuild`.
  - *Production Stage*: Minimal alpine runtime, runs under an unprivileged `appuser` (UID 1001) for container security.
- **Reverse Proxy & Routing**: Docker Compose configuration integrating **Traefik** as a reverse proxy with automated Let's Encrypt SSL certificates and HTTP-to-HTTPS redirection.
- **Static Asset Optimization**: Express serves compiled assets with immutable cache headers (`max-age=31536000`), while ensuring `index.html` is served with `no-cache` to enable zero-downtime updates.

---

## 14. Key Engineering Challenges & Solutions

### Challenge 1: LLM Latency & User Experience in Chat Widgets
*Problem*: Generating responses from large models combined with multi-document RAG retrieval introduced 3-5 second delays before visitors saw any feedback.  
*Solution*: Implemented token streaming using chunked HTTP responses and Server-Sent Events (SSE). The UI begins rendering response tokens within 350ms, while vector retrieval is executed in parallel with system prompt preparation.

### Challenge 2: Client CSS Conflicts on Third-Party Websites
*Problem*: When embedding the chat widget on diverse sites (e.g., sites with aggressive `* { box-sizing: border-box; margin: 0; }` or low-specificity resets), widget buttons and chat frames suffered visual distortion.  
*Solution*: Re-architected `widget.js` to mount within a closed **Shadow DOM**. By encapsulating styles inside a Shadow Root and isolating the chat frame inside a secure iframe, widget styles remain 100% immune to host-page CSS leaks.

### Challenge 3: Balancing Data Ingestion with API Token Costs
*Problem*: Scraping large commercial websites frequently generated hundreds of kilobytes of boilerplate HTML (navbars, scripts, footers), overloading embedding token limits.  
*Solution*: Created an intelligent server-side HTML parser with Cheerio that strips non-semantic elements (`nav`, `footer`, `script`, `style`, `svg`), normalizes whitespace, and falls back to OpenGraph meta tags if the page is a sparse Single-Page App shell.

---

## 15. Summary of Demonstrated Capabilities

- **Production AI Application Engineering**: Real-world RAG implementation using Postgres `pgvector`, multi-model orchestrations (Cohere + Google Gemini), and dynamic LLM tool calling.
- **Full-Stack Systems Architecture**: Seamless integration of a modern React 18 frontend with a hardened Express backend and managed Postgres.
- **Defensive Cyber-Security**: End-to-end implementation of session fingerprinting, rate limiting, anti-SSRF validation, input sanitization, and brute-force mitigation.
- **Product & SaaS Craftsmanship**: Thoughtful user experiences, zero-dependency widget integrations, transactional communications, and strict GDPR privacy engineering.
