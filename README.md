# SkillSprint IQ: Multi-Agent Certification Readiness Assistant

SkillSprint IQ is a local multi-agent demo project built for the **Agents League Hackathon — Reasoning Agents track**.

It helps enterprise learning teams plan certification readiness using synthetic learner data, workload signals, certification requirements, and manager-level readiness rules.

> Demo status: Working local multi-agent app  
> Cloud status: Microsoft Foundry / Foundry IQ integration plan documented  
> Data status: Synthetic data only

---

## Problem

Organisations often manage certification programmes across multiple roles, teams, and workloads.

Managers need to know:

- Which learners are ready
- Which learners are at risk
- What study plan is realistic
- Which team needs support
- What action should be taken before exam scheduling

SkillSprint IQ turns scattered learning and workload signals into simple, manager-friendly recommendations.

---

## Solution

SkillSprint IQ uses a small multi-agent system to help with certification readiness planning.

The app can:

- Recommend a learning path by role and certification
- Generate a workload-aware study plan
- Identify readiness risk at team level
- Suggest manager actions
- Use synthetic documents and CSV files as the local knowledge base

---

## Challenge Alignment

This project is aligned to the **Reasoning Agents** challenge scenario: an enterprise learning and certification readiness system.

The project demonstrates:

- Multi-agent design
- Agent orchestration
- Multi-step reasoning
- Synthetic data usage
- Manager-level readiness insight
- Responsible AI and data safety documentation
- Microsoft Foundry / Foundry IQ integration plan

---

## Agents

| Agent | Responsibility |
|---|---|
| Orchestrator Agent | Receives the user question and routes it to the correct specialist agent |
| Learning Path Curator Agent | Maps learner role and certification target to required skills and recommended study hours |
| Study Plan Generator Agent | Creates a realistic study plan using learner progress and workload signals |
| Manager Insights Agent | Summarises team readiness, at-risk learners, and recommended manager action |
| Assessment Agent | Planned extension for grounded practice questions |

---

## How the Multi-Agent Flow Works

```text
User question
   ↓
Orchestrator Agent
   ↓
Specialist Agent
   ├─ Learning Path Curator Agent
   ├─ Study Plan Generator Agent
   └─ Manager Insights Agent
   ↓
Synthetic data + synthetic knowledge documents
   ↓
Reasoned response