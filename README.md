# 🤖 AI Job Search Agent

An AI-powered job search agent that converts natural-language job search queries into structured search criteria, searches LinkedIn, extracts job information, and fetches detailed job descriptions.

The project is being built incrementally with Python, FastAPI, LangChain, Playwright, Pydantic, and BeautifulSoup.

> 🚧 **Project Status:** In Progress

---

## 🎯 Goal

The goal of this project is to build an intelligent job-search agent that can eventually:

- Understand natural-language job search queries
- Search multiple job platforms
- Extract and normalize job information
- Fetch detailed job descriptions
- Extract required skills and experience
- Match jobs against a candidate's profile
- Rank jobs based on relevance
- Provide job application recommendations
- Eventually assist with the application workflow

---

## 🏗️ Current Architecture

```text
User
 │
 │ Natural-language query
 ▼
FastAPI Endpoint
 │
 ▼
Query Parser
 │
 │ Structured JobSearchRequest
 ▼
Job Search Service
 │
 ▼
LinkedIn Source
 │
 ├── Build LinkedIn Search URL
 │
 ├── Fetch Search HTML
 │
 ├── Parse Job Cards
 │
 └── Extract Job Information
 │
 ▼
Job[]
 │
 ▼
Build Job Detail URL
 │
 ▼
Playwright + Chrome
 │
 ▼
Rendered Job Page
 │
 ▼
BeautifulSoup
 │
 ▼
Job Description
