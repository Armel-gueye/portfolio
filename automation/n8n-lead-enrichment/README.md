# Automated Lead Collection & Enrichment

## Production Lead Collection Pipeline

This n8n workflow automates the collection, extraction, enrichment, qualification, routing, and storage of business leads.

It combines web data collection, scraping, AI-assisted analysis, structured extraction, validation, database operations, and error handling.

## End-to-End Flow

```text
Telegram Request
      ↓
Google Maps Data Collection
      ↓
JavaScript Processing
      ↓
Website Detection / Crawling
      ↓
Contact & Business Data Extraction
      ↓
AI-Assisted Qualification
      ↓
Phone / Data Validation
      ↓
Service Classification & Routing
      ↓
Supabase / PostgreSQL
      ↓
Notifications / Error Handling
```

## What I Built

- Telegram-triggered workflow execution
- Business discovery from Google Maps data
- Website crawling with Crawl4AI
- Lead data extraction and enrichment
- Email, phone, website, and social-profile extraction
- AI-assisted data interpretation and qualification
- Phone validation and normalization
- Conditional service routing
- Batch and loop processing
- Structured-output validation
- PostgreSQL / Supabase persistence
- Upsert and duplicate/conflict handling
- Error-triggered Telegram notifications

## Main Integrations

| Category | Services / Technologies |
| --- | --- |
| Automation | n8n |
| Business Data | Apify / Google Maps |
| Web Scraping | Crawl4AI |
| AI | Cohere, AI agents / LLM chains |
| Database | PostgreSQL, Supabase |
| Trigger & Alerts | Telegram |

## Technical Design

The workflow contains multiple JavaScript transformation stages, scraping branches, AI analysis chains, structured-output parsing, loops, waits, conditional routing, SQL operations, and error handling.

It also separates processing based on business context and service needs, allowing different lead categories to be routed to different downstream paths.

## Visual Evidence

![Lead Collection & Enrichment Workflow](../../assets/n8n/BDL%20Leads%20scraper%20workflow.png)

## Workflow JSON

[workflow.json](workflow.json)

## Skills Demonstrated

Workflow automation, web scraping, data extraction and enrichment, AI-assisted qualification, JavaScript data processing, structured outputs, conditional routing, SQL/Supabase operations, batch processing, and operational error handling.
