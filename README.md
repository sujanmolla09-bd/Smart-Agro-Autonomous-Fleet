# 🌾 Smart Agro Autonomous Operations Fleet (Good Neighbor Edition)

An autonomous multi-agent system built for the **AWS Agents for Humans Hackathon** (Good Neighbor Track). Powered by **AWS Strands SDK**, **Gemini AI**, and **Google Cloud Infrastructure**.

---

## 🚀 Overview

The **Smart Agro Autonomous Operations Fleet** automates background agricultural decision-making and community resilience by coordinating specialized AI agents. Using **AWS Strands SDK** for agent communication and orchestration alongside **Gemini AI** for deep reasoning, it continuously monitors field telemetry, performs risk analysis, and triggers automated community fleet actions without requiring direct manual input.

---

## 🤖 Multi-Agent Architecture

```text
[ Sensor Telemetry ]
        │
        ▼
┌───────────────────┐
│   Data Collector  │ ─── (Gathers soil & weather data via AWS Strands SDK)
└───────────────────┘
        │  (A2A Protocol / Strands Agent Channel)
        ▼
┌───────────────────┐
│   Agro Analyzer   │ ─── (Gemini AI Evaluation & Spatial Reasoning)
└───────────────────┘
        │  (A2A Protocol / Strands Agent Channel)
        ▼
┌───────────────────┐
│  Action Executor  │ ─── (Triggers automated irrigation, machinery & fleet alerts)
└───────────────────┘
