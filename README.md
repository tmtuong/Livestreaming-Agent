# 🤖 AI Marketing Agent — Automated TikTok LIVE Comment Analysis & Response

> An AI agent that reads, classifies, prioritizes and drafts responses for real-time TikTok LIVE comments — built for L'Oréal Paris Vietnam as a case study.

![Make.com](https://img.shields.io/badge/Make.com-No--Code-6D00CC?logo=make&logoColor=white)
![DeepSeek](https://img.shields.io/badge/DeepSeek-LLM-blue)
![Google Sheets](https://img.shields.io/badge/Google%20Sheets-Output-34A853?logo=google-sheets&logoColor=white)

---

## 📌 Introduction

TikTok LIVE commerce is booming in Vietnam — **39.6% TikTok Shop market share** (2025), with live streams generating **35–40% of direct sales revenue** in Southeast Asia. But during a live session, **dozens of comments flood in every minute**, each lasting only a few minutes in value. Brands that can't respond fast enough lose customers: **73% of consumers switch to competitors** if they don't get timely responses.

This project builds an **AI Marketing Agent** — not a chatbot, but an autonomous system that perceives, reasons, plans, and acts — to process TikTok LIVE comments in real-time. It analyzes sentiment, classifies intent, scores priority, and generates safe draft responses for human review.

**Case Study:** L'Oréal Paris Vietnam TikTok LIVE  
**Platform:** Make.com (no-code automation)  
**LLM:** DeepSeek (batch processing)  
**Tested on:** 80 real comments across 3 live batches

---

## 🔥 The Pain Point

During a TikTok LIVE session, brands face a unique challenge that traditional customer service tools can't solve:

1. **Volume & Speed** — Comments appear at dozens per minute, each with a lifespan of only a few minutes
2. **Unstructured & Noisy** — Vietnamese slang, abbreviations, mixed languages, emojis, and typos
3. **Multiple Intents** — A single comment may ask about price, product quality, AND promotions simultaneously
4. **High Stakes** — 84% of consumers say response speed directly impacts brand perception (Sprout Social, 2025)
5. **No Existing Solution** — Current tools handle fanpage/website comments (async, structured) — not live stream comments (real-time, chaotic)

> Manual processing is impossible at scale. But fully automated responses are too risky for a premium beauty brand. The solution must be **fast, intelligent, and human-supervised**.

---

## 💡 Core Idea

Build an AI Agent (not a chatbot) that follows the **Perceive → Reason → Act** framework:

```
Comments In → Batch Aggregation → AI Analysis → Priority Routing → Draft Responses → Human Review
```

Key design decisions:
- **Agent, not chatbot:** Proactively processes all comments in batches, doesn't wait for triggers
- **Human-in-the-loop:** Never auto-replies — all outputs go to Google Sheets for human approval
- **Guardrails first:** Won't fabricate prices, won't make medical claims, won't promise unavailable promotions
- **Role-based output:** Different outputs for live host, customer service, and marketing teams

### The AI Agent produces 6 analysis layers per comment:

| Layer | Output | Example |
|-------|--------|---------|
| **Sentiment** | Positive / Neutral / Negative | "Sản phẩm tốt lắm!" → Positive |
| **Intent** | 1 of 8 labels | Inquiry, Price, Promotion, Evaluation, Logistics, Host, Chat, Other |
| **Aspect Labels** | Up to 9 aspects | Product quality, Price, Packaging, Delivery, etc. |
| **Priority** | 1–5 score with reasoning | Price complaint during flash sale → Priority 5 |
| **Confidence** | High / Medium / Low | Indicates AI certainty for human reviewers |
| **Response Scenario** | 1 of 10 templates | Safe draft aligned to brand voice |

---

## ⚙️ Implementation

### Architecture: 5-Layer Pipeline on Make.com

```
Input → AI Agent → Tools → Decision → Action
```

**Layer 1 — Input:** Custom webhook receives comments from TikTok LIVE (batches of up to 30)

**Layer 2 — AI Agent:** Aggregator collects comments → JSON Transform → DeepSeek LLM processes entire batch with structured prompt (temperature=0.2 for consistency)

**Layer 3 — Tools:** Parse JSON → Iterator splits into individual records → Feeder extracts structured fields

**Layer 4 — Decision:** Main Router + Sub-routers classify each comment by sentiment and priority:
- Negative sentiment → Draft safe response for CS team
- Positive sentiment → Flag as social proof opportunity for marketing
- High priority (4–5) → Route to priority queue
- Price/promotion queries → Flag for verification (no AI-generated numbers)

**Layer 5 — Action:** Write to **8 Google Sheets tables**:
- Run Summary, Customer Cases, Priority Queue, CS Responses, Positive Content, User Window, Host Events, Aspect Recommendations

### 7-Step Processing Flow

1. **Comment appears** during LIVE session
2. **Webhook collects & transmits** data in standardized format
3. **Batch aggregation** — up to 30 comments per batch, serialized as JSON
4. **AI Agent analyzes** — reads full batch, builds customer profiles, assigns all 6 labels
5. **Action generation** — drafts responses, content ideas, or promotion suggestions
6. **Decision routing** — directs each case to the appropriate output table
7. **Results recorded** — saved to Google Sheets with "pending review" status

### Safety Guardrails
- ❌ Never fabricates prices or discount percentages
- ❌ Never makes skin/health claims without verification
- ❌ Never auto-sends responses — all drafts require human approval
- ✅ Three approval statuses: Pending → Approved → Rejected
- ✅ Confidence scores help reviewers prioritize manual checks

---

## 📊 Key Results

### Real-World Testing: 3 Batches from L'Oréal Paris TikTok LIVE

| Metric | Batch 1 | Batch 2 | Batch 3 | Total |
|--------|---------|---------|---------|-------|
| **Timestamp** | 12/09 19:21 | 12/09 20:25 | 13/09 12:02 | — |
| **Comments** | 30 | 30 | 20 | **80** |
| **Cases Generated** | 18 | 20 | 16 | **54** |
| **High Priority** | 0 | 0 | 2 | **2** |

### Key Findings
- **54 customer cases** extracted from 80 comments — each with sentiment, intent, aspects, priority, and draft response
- **Most cases contained 1–2 comments** (38 single-comment cases), showing effective deduplication
- **2 high-priority cases** correctly identified in Batch 3 (price complaints during promotion)
- **Batch 4 edge case** (0 comments) revealed need for empty-batch handling

### SWOT Assessment
- **Strengths:** Scalable batch processing, customer-level analysis, safe guardrails, low-cost no-code deployment
- **Weaknesses:** Prompt-dependent output quality, no real-time price/promo database connection
- **Opportunities:** Expandable to fanpage, website, and other e-commerce platforms
- **Threats:** Third-party LLM dependency, hallucination risk for product claims

---


## 🛠️ Tech Stack

- **Automation Platform:** Make.com (no-code iPaaS)
- **LLM:** DeepSeek (via API, batch mode, temperature=0.2)
- **Data Storage:** Google Sheets (8 output tables, human review interface)
- **Input:** Custom Webhook (TikTok LIVE comment feed)
- **Concepts:** AI Agent framework, Sentiment Analysis, ABSA, Intent Classification, Priority Scoring, Human-in-the-Loop

---

## 📄 License

This project is for educational and portfolio purposes. L'Oréal Paris is used as a case study brand for academic research only.
