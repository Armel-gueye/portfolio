# Kouma

## Production RAG-Based AI Platform

**Live application:** https://kouma.app

Kouma is a **live, production conversational AI SaaS platform** built around Retrieval-Augmented Generation (RAG), document processing, vector search, AI integrations, and an embeddable website chatbot.

It is a real deployed application with a complete product and infrastructure layer rather than a proof-of-concept chatbot.

## Product

Kouma enables businesses to create and deploy context-aware AI assistants grounded in their own knowledge.

### Main capabilities

- AI chatbot creation and configuration
- Visual bot customization
- PDF and document ingestion
- Website content scraping and knowledge extraction
- RAG-based retrieval using vector embeddings
- Multiple AI provider integrations
- Streaming conversations
- Autonomous lead capture through function calling
- Conversation history and lead inbox
- Embeddable website widget
- Transactional email notifications
- Account and privacy management

## Production Architecture

```text
Website Visitor
      │
      ▼
Embeddable Kouma Widget
      │
      ▼
React Application
      │
      ▼
Node.js / Express Backend
      │
      ├── RAG / Vector Search
      ├── Cohere
      ├── Google Gemini
      ├── Resend
      ├── Supabase / PostgreSQL
      └── Security / Observability
```

The application uses a React frontend, Node.js/Express backend, Supabase/PostgreSQL with pgvector, Cohere and Google Gemini, and supporting infrastructure for secure deployment and monitoring.

## Production & Operations

Kouma includes the operational components expected from a real SaaS application:

- Authentication and protected application areas
- Automated transactional email delivery
- Persistent application, conversation, and lead data
- Vector storage and retrieval infrastructure
- Application error monitoring
- Git-based version control
- Docker containerization
- VPS deployment with Docker Compose and Traefik
- HTTPS and reverse-proxy configuration
- Rate limiting and abuse controls
- SSRF protection for website scraping
- Input sanitization and security validation
- Privacy and account-deletion flows

The system is designed as a production application for real business use and continued growth.

## RAG Pipeline

```text
Documents / Website Content
            │
            ▼
Text Extraction & Cleaning
            │
            ▼
Chunking & Metadata
            │
            ▼
Embeddings
            │
            ▼
Supabase / pgvector
            │
            ▼
Similarity Search
            │
            ▼
Relevant Context
            │
            ▼
LLM Response
```

This architecture grounds chatbot responses in indexed business information instead of relying only on generic model knowledge.

## My Role

I worked on the architecture and implementation of the application, including:

- Full-stack application development
- RAG pipeline implementation
- Document processing
- Vector search integration
- LLM integrations
- Function calling and lead capture
- Embeddable widget architecture
- Authentication and security
- Database integration
- Transactional communication
- Deployment and infrastructure configuration
- Testing and iterative product development

The development workflow was AI-assisted, with technical implementation and system behavior validated during development.

## Technology Stack

| Layer | Technologies |
| --- | --- |
| Frontend | React 18, TypeScript, Vite, Tailwind CSS |
| Backend | Node.js 20+, Express |
| AI | Cohere, Google Gemini |
| RAG | Embeddings, pgvector, PostgreSQL |
| Database & Auth | Supabase |
| Email | Resend |
| Security | Zod, SSRF protection, rate limiting, input sanitization |
| Observability | Sentry |
| Infrastructure | Docker, Docker Compose, Traefik, VPS |
| Version Control | Git / GitHub |

## Visual Evidence

### Application

![Kouma](../../assets/kouma/Kouma.png)

![Kouma](../../assets/kouma/Kouma%20%282%29.png)

![Kouma](../../assets/kouma/Kouma%20%283%29.png)

![Kouma](../../assets/kouma/Kouma%20%284%29.png)

![Kouma](../../assets/kouma/Kouma%20%285%29.png)

### Architecture

![Kouma Architecture](../../assets/kouma/Kouma%20Architecture%20Diagram.png)

## Technical Documentation

**Full technical overview:** [Kouma Technical Overview](Kouma-Technical-Overview.md)

The technical overview provides a deeper description of the architecture, RAG implementation, AI integrations, API design, security model, deployment, and engineering decisions.

## Public Portfolio Scope

This repository contains public-safe documentation and visual evidence. Credentials, API keys, authentication secrets, private infrastructure details, and proprietary source code are intentionally excluded.