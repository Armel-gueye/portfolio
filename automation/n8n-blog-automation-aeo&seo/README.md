# n8n AI Content & AEO Automation

## Production Content Automation Pipeline

This workflow is a real automation system used to support BinkoO Digital Lab's content production process.

It connects research, AI-assisted writing, SEO/AEO enrichment, media handling, WordPress publication, indexing-related actions, database operations, scheduling, and monitoring into one automated pipeline.

## End-to-End Flow

```text
Scheduled / Manual Trigger
        ↓
Research & Topic Selection
        ↓
AI Synthesis & Article Generation
        ↓
SEO / AEO Enrichment
        ↓
FAQ + Structured Data
        ↓
Image / Media Processing
        ↓
WordPress Publication
        ↓
Sitemap / Indexing Actions
        ↓
Telegram Notifications & Monitoring
```

## What I Built

- Scheduled and manual workflow execution
- Automated topic and headline selection using data and research signals
- AI-assisted article synthesis and writing
- SEO and AEO enrichment
- FAQ and Schema.org JSON-LD generation
- Content cleaning and formatting with JavaScript
- Image search and media processing
- WordPress REST API publishing
- Database queries and content history tracking
- Sitemap/build-related automation
- Search indexing-related requests
- Telegram notifications
- Error-triggered monitoring and notifications

## AI & Service Integrations

| Category | Services / Technologies |
| --- | --- |
| Automation | n8n |
| AI | Google Gemini, Cohere |
| Research | Exa, Google Suggestions |
| Content | WordPress REST API |
| Database | PostgreSQL |
| Media | Unsplash |
| Deployment / Build | Netlify |
| Notifications | Telegram |
| Indexing | Google Indexing API |

## Technical Design

The workflow contains JavaScript transformation and decision nodes, LLM chains and agents, PostgreSQL operations, merges, loops, waits, scheduled execution, conditional routing, and explicit error handling.

It is not simply an AI prompt connected to WordPress. It orchestrates multiple stages and services to produce, enrich, publish, and monitor content with minimal manual intervention.

## Connection to the BinkoO Website

This workflow is directly connected to the BinkoO Digital Lab website.

Articles produced by the workflow are sent to WordPress, and the BinkoO website then presents the published content through its own designed blog experience.

See the complete project: [BinkoO Digital Lab](../../projects/binkoo-digital-lab/README.md).

## Visual Evidence

![n8n AI Content & AEO Workflow](../../assets/n8n/Wordpress%20Blog%20automation.png)

## Workflow JSON

[workflow.json](workflow.json)

The published JSON should remain sanitized of credentials, tokens, private endpoints, secrets, and other sensitive configuration.

## Skills Demonstrated

n8n workflow automation, generative AI integration, LLM orchestration, API integration, JavaScript data transformation, PostgreSQL, WordPress automation, SEO/AEO content systems, scheduling, routing, monitoring, and error handling.