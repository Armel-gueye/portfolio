# AEOBoost — Public Technical Overview

> **Document Classification:** Public Technical Portfolio Document  
> **Target Audience:** Engineering Leads, Technical Recruiters, System Architects  
> **Project Scope:** Answer Engine Optimization (AEO) & Generative Engine Optimization (GEO) SaaS Platform  
> **Author Role:** Full-Stack & AI Systems Developer  

---

## 1. Project Overview and Purpose

**AEOBoost** (`aeoboost.app`) is a B2B SaaS platform engineered for SEO consultants, marketing agencies, and digital brands transitioning from traditional Search Engine Optimization (SEO) into **Answer Engine Optimization (AEO)** and **Generative Engine Optimization (GEO)**.

While traditional search indexes pages based on link graphs and keyword matching, modern LLMs (ChatGPT, Perplexity, Claude, Google Gemini, DeepSeek) synthesize direct answers using citation retrieval, structured semantic knowledge, and domain authority. AEOBoost enables businesses to:
1. **Audit Technical AEO Readiness:** Analyze websites across 7 weighted architectural pillars required for LLM ingestibility and citation.
2. **Simulate Real-Time LLM Queries & Citation Tracking:** Test target keyword queries across multiple frontier AI engines to determine whether a brand is cited, how it is recommended, and which competitors are favored.
3. **Automate Remediation:** Generate machine-readable markdown exports, llms.txt configurations, schema recommendations, and executive PDF reports.

---

## 2. Main Features

* **Instant Public Audit (Try-Before-Signup):**
  * A public landing page audit providing instant technical evaluation of the 7 AEO pillars without requiring immediate account creation.
  * Protected by multi-layer anti-bot verification, concurrency throttling, and an automated FIFO queuing system.

* **7-Pillar Technical AEO Scoring Engine:**
  * Evaluates web architecture against verified criteria:
    * **E-E-A-T & Brand Trust (25%):** Author signatures, schema entities (`Person`, `Organization`), editorial credibility.
    * **Structured Data & Schema.org (20%):** JSON-LD graphs, Article, Product, FAQPage, and Organization schemas.
    * **Content Freshness & Timestamps (15%):** ISO 8601 published/modified timestamps and freshness signals.
    * **Authoritative Citations & External Sources (15%):** Reference density, out-of-domain citations, and academic/industry signals.
    * **Semantic Hierarchy (10%):** Strict heading trees (H1–H4), structured tables, lists, and summary extractability.
    * **Comparative & Commercial Signals (10%):** Pricing tables, feature matrices, pros/cons, and alternative analysis.
    * **AI Crawler Accessibility (5%):** Verification of `robots.txt` permissions for primary AI user-agents (`GPTBot`, `PerplexityBot`, `ClaudeBot`, `Google-Extended`).

* **Multi-Model LLM Citation Testing:**
  * Parallel querying of target keywords across leading AI models (Claude 3.5/Sonnet, GPT-4o, Gemini Flash/Pro, Perplexity Sonar with live web search, DeepSeek, and Cohere Command R+).
  * Measures citation probability, recommendation sentiment (positive, neutral, negative), and positioning.

* **Autonomous In-Memory Competitor Extraction:**
  * Proprietary deterministic brand extractor that identifies competing software solutions directly from LLM responses without secondary AI calls (0 additional API tokens, sub-millisecond execution).

* **Reporting & Export Suite:**
  * LLM-optimized Markdown exports designed for ingestion into ChatGPT Custom GPTs or Claude Projects.
  * Client-ready PDF generation with visual scoring cards, remediation roadmaps, and white-label agency options.

* **Developer-Friendly Git-Based Blog & AEO Knowledge Hub:**
  * Fully markdown-driven content architecture rendered via dynamic client/server processing with RSS/Sitemap auto-generation on build.

---

## 3. Role and Core Contributions

As the core developer responsible for the platform's architecture and full-stack implementation, contributions included:

* **End-to-End Architecture Design:** Designed the complete system topology including the React frontend, Node.js/Express Backend-for-Frontend (BFF), Supabase integration, and external crawler orchestration.
* **Backend Pipeline & Security Engineering:** Built the proxy layer to protect third-party API credentials, implemented strict SSRF guards with DNS resolution checks, developed an in-memory FIFO queue for concurrency management, and integrated Cloudflare Turnstile verification.
* **AEO Evaluation Algorithms:** Developed the weighted 7-pillar evaluation logic and the heuristic named-entity brand extractor.
* **LLM Orchestration:** Architected multi-model integration supporting OpenRouter, Google Gemini SDK, and Cohere APIs with automatic failover mechanisms.
* **Data Layer & Authentication:** Configured PostgreSQL tables, user profiles, session cookie token handling, and database interactions through Supabase.

---

## 4. Frontend and Backend Technologies

### Frontend Architecture
* **Framework:** React 18 with TypeScript and Vite.
* **Routing:** React Router DOM (v7) with route guards for authenticated dashboards, onboarding funnels, and public tools.
* **Styling & Design System:** Tailwind CSS with typography, container-queries, and forms plugins. Neobrutalist design accents with high-contrast surfaces and accessible WCAG AA color palettes.
* **Motion & Interactivity:** `motion` (Motion for React) and GSAP for micro-interactions and scroll reveal animations.
* **Data Visualization:** Recharts for historical metrics, trend lines, and pillar distribution radar charts.
* **Document Generation:** `jspdf` and `html2canvas` for client-side PDF compilation; `marked` and `react-markdown` for markdown processing.

### Backend-for-Frontend (BFF) Architecture
* **Runtime:** Node.js (ES Modules) with Express.
* **Middleware Stack:** Helmet for HTTP security headers, CORS configuration, Cookie Parser, Body Parser, and Express Rate Limit.
* **Serving Strategy:** Express serves REST API endpoints under `/api/*` and acts as the SPA host serving the production Vite build in production, with Vite development middleware mounted in local environments.

---

## 5. Database and Data Architecture

The application uses **Supabase (PostgreSQL)** for persistence, accessed through the official `@supabase/supabase-js` client with Row-Level Security (RLS) policies.

### High-Level Data Models:
* **Users & Profiles (`profiles`):** Extends Supabase Auth users, tracking tier status, audit quotas, and agency settings.
* **Projects & Domains (`projects`, `project_modules`):** Multi-domain project management grouping domain audits, competitors, and module statuses.
* **AEO Audit History (`aeo_website_audits`, `aeo_keywords_audits`):** Stores timestamped audit records, 7-pillar breakdown scores, raw crawler metadata, and recommendations.
* **Citation Tracking & Time-Series Metrics (`aeo_tests`, `aeo_daily_metrics`):** Captures individual model test outputs, competitor frequencies, sentiment scores, and historical visibility trends.
* **Onboarding & Badges (`onboarding_answers`, `user_badges`):** Tracks user profile configuration and platform milestones.

---

## 6. AI/LLM Components and Usage

AEOBoost utilizes LLMs strategically across different stages of analysis:

1. **Multi-Model Evaluation via OpenRouter:**
   * Acts as the primary aggregator to query `openai/gpt-4o`, `anthropic/claude-sonnet-4.6`, `google/gemini-3.5-flash`, `perplexity/sonar-pro-search`, and `deepseek/deepseek-chat`.
   * Standardizes multi-vendor prompt templates and normalizes unstructured LLM responses into structured citation scores.

2. **Google GenAI SDK (`@google/genai`):**
   * Server-side fallback engine initialized with native API keys.
   * Provides rapid fallback reasoning if aggregator services experience downtime or rate-limit saturation.

3. **Google Cloud Dialogflow CX / Gemini Agent Integration:**
   * Utilizes `@google-cloud/dialogflow-cx` sessions with Application Default Credentials (ADC) for conversational search simulations.

4. **Cohere API Integration (`cohereClientV2`):**
   * Command R+ integration for semantic evaluation, classification, and reranking tasks.

5. **Heuristic Zero-Token Competitor Extractor:**
   * Rather than making costly secondary LLM calls to parse competitors from simulation responses, a server-side heuristic dictionary and title-cased entity parser extracts commercial brands in `O(n)` time at zero additional cost.

---

## 7. APIs and Important External Services

* **Headless Web Crawling (Crawl4AI via n8n webhook):**
  * Asynchronously scrapes target URLs to extract clean markdown, DOM heading structures, JSON-LD schemas, image alt coverage, and robots directives.
  * Features a circuit breaker pattern (60-second cooldown) to avoid cascading server delays during crawler downtime.
* **Google PageSpeed Insights API:** Proxied server-side to extract real-world Core Web Vitals (LCP, CLS, FID) without exposing keys to the browser.
* **Cloudflare Turnstile:** Privacy-focused CAPTCHA verification preventing malicious automated crawling on public endpoints.
* **PostHog:** Product analytics tracking user acquisition, audit funnels, and subscription milestones.

---

## 8. Authentication and User Management

* **Provider:** Supabase Auth (JWT-based).
* **Architecture:** Hybrid cookie and Bearer token model.
  * Client maintains Supabase auth state while requests to the backend pass tokens via HTTP cookies (`sb-access-token`) or `Authorization: Bearer <token>` headers.
  * Server-side `requireAuth` middleware validates tokens against `supabase.auth.getUser(token)` before permitting access to protected routes.
* **CSRF Mitigation:** Custom Double Submit Cookie / header verification (`x-csrf-token`) applied to state-changing operations.
* **Account Lifecycle:** Complete signup, login, password reset flow, and role validation.

---

## 9. Analytics and Observability

* **Product Analytics (PostHog):** Dual-layer tracking (client-side `analytics.ts` and server-side `posthog-node`). Tracks critical funnel events (`signup_completed`, `authenticated_audit_completed`, `public_audit_run`, `domain_added`).
* **Structured Server Logging (`serverLogger.js`):** Modular logger with log levels (`debug`, `info`, `warn`, `error`) capturing request context, latency, IP addresses (hashed/masked where appropriate), and security events.
* **Deterministic Synchronized Metrics:** Mathematical pseudo-random generator (`mulberry32`) synchronized against a fixed epoch to simulate global platform crawler activity consistently across all visitors without database overhead.

---

## 10. Deployment and Hosting Architecture

* **Container Runtime:** Containerized deployment (Docker) on **Google Cloud Run** (managed serverless container platform) with auto-scaling capabilities.
* **Reverse Proxy:** Internal routing bound to host `0.0.0.0` and port `3000`.
* **Automated Build Pipeline:**
  * Custom build script (`npm run build`) runs `generate-sitemap.js` (extracting metadata from all Markdown articles into XML) followed by `vite build`.
  * Production server launched with Node.js running `server.js`.

---

## 11. Technical Decisions and Architectural Challenges

### Challenge 1: Public Crawler Abuse & Resource Exhaustion
* **Problem:** Running full site crawls and AI audits for unauthenticated visitors introduces high server load, potential IP bans, and vendor cost spikes.
* **Solution:** Implemented a defense-in-depth architecture:
  1. Honeypot fields detecting naive bot submissions.
  2. Cloudflare Turnstile token validation on the backend.
  3. IP rate limiting (1 audit / IP / 24h for guests).
  4. In-memory FIFO queue capping concurrent public crawls at strictly **3 simultaneous executions**, queuing subsequent requests with automatic timeout and client disconnect handling.

### Challenge 2: Server-Side Request Forgery (SSRF) Prevention
* **Problem:** Allowing users to submit arbitrary URLs to be fetched by internal services could expose internal network metadata endpoints (e.g., AWS/GCP metadata services).
* **Solution:** Created strict URL validation that:
  1. Restricts protocols strictly to `http:` and `https:`.
  2. Disallows non-standard ports (allowing only 80 and 443).
  3. Blocks loopback, RFC 1918 private ranges, and cloud metadata hostnames (`169.254.169.254`, `metadata.google.internal`).
  4. Resolves hostnames via `dns.lookup()` before requesting and verifies that the resolved IP address does not point to a restricted subnet (defense against DNS rebinding).

### Challenge 3: Eliminating Redundant LLM Costs
* **Problem:** Asking an LLM to identify and list competitors from a previous answer simulation required a second round-trip LLM prompt for every test keyword.
* **Solution:** Built an autonomous in-memory entity extractor using a curated stopword set and known-brand normalization dictionary. Reduced API token consumption by ~50% per keyword test.

---

## 12. Security Considerations

* **Credential Isolation:** All API keys (OpenRouter, Gemini, Cohere, PageSpeed, Turnstile Secret, Supabase Service keys) are stored server-side in environment variables and are never bundled into client-side code.
* **Strict CORS & HTTP Security Headers:** Helmet is configured with tailored Content Security Policies (CSP), frameguard rules, and cross-origin controls.
* **Input Sanitization & Length Limits:** Centralized validation library enforcing strict regex patterns and character length maximums across all user-supplied inputs.
* **Zero AI Training Lock:** Platform ensures audited client data is explicitly flagged to prevent retention for public model training.

---

## 13. Current Limitations and Roadmap

* **Single-Page Crawl Focus:** Current technical audits evaluate the submitted URL/landing page; expanding to automated multi-page deep site crawls is planned.
* **Web-Search Grounding Latency:** Multi-model testing that includes live web search (e.g., Perplexity Sonar) takes 4–8 seconds per query due to real-time search synthesis.
* **Scheduled Automated Re-Auditing:** Background cron worker infrastructure for automated weekly citation tracking is designed and ready for background job queue integration (e.g., BullMQ / Cloud Tasks).

---

## 14. Concise Technology Stack

| Layer | Technology |
| :--- | :--- |
| **Frontend** | React 18, TypeScript, Vite, Tailwind CSS, Motion (motion/react), Recharts, Lucide Icons |
| **Backend / BFF** | Node.js (ESM), Express, Helmet, Express Rate Limit, Cookie Parser |
| **Database & Auth** | Supabase (PostgreSQL), Row Level Security (RLS), JWT Authentication |
| **AI / LLM Providers** | OpenRouter (Claude, GPT-4o, Perplexity, DeepSeek), Google GenAI SDK (Gemini), Cohere Command R+, Google Cloud Dialogflow CX |
| **Web Crawling** | Crawl4AI via n8n webhook orchestration with circuit breaker protection |
| **Bot Mitigation** | Cloudflare Turnstile (`@marsidev/react-turnstile` + server-side verification) |
| **Analytics** | PostHog (Client-side & Server-side SDK) |
| **Infrastructure** | Google Cloud Run, Docker, Automated XML Sitemap Generator |

---

*This summary was compiled from verifiable codebase architecture, route definitions, and configuration files of the AEOBoost platform.*
