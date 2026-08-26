# 🌾 Smart Agro Autonomous Operations Fleet
An autonomous multi-agent system built for the **Google All Things Agentic Hackathon**. Powered by **Google ADK**, **Agent-to-Agent (A2A) Protocol**, and **Google Cloud Run**.

---

## 🚀 Overview
The **Smart Agro Autonomous Operations Fleet** automates background agricultural decision-making by coordinating specialized AI agents. It continuously monitors field telemetry, performs intelligent risk analysis using Gemini AI, and triggers automated field infrastructure actions.

---

## 🤖 Multi-Agent Architecture
```text
[ Sensor Telemetry ] 
         │
         ▼
 ┌──────────────────────┐
 │  Data Collector      │ ── (Gathers soil & weather data)
 └──────────┬───────────┘
            │  (A2A Protocol)
            ▼
 ┌──────────────────────┐
 │  Agro Analyzer       │ ── (Gemini AI Evaluation)
 └──────────┬───────────┘
            │  (A2A Protocol)
            ▼
 ┌──────────────────────┐
 │  Action Executor     │ ── (Triggers irrigation & logs events)
 └──────────────────────┘
