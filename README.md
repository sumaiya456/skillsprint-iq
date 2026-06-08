# SkillSprint IQ: Multi-Agent Certification Readiness Assistant

SkillSprint IQ is a hackathon project for the Agents League Reasoning Agents track.

It is a synthetic multi-agent enterprise learning system that helps teams plan certification learning, generate workload-aware study plans, and surface manager-level readiness risks.

## Problem

Enterprise learning teams often manage certification programmes across different roles, workloads, and readiness levels. Managers need a simple way to understand who is ready, who is at risk, and what action to take next.

## Solution

SkillSprint IQ uses a multi-agent design to coordinate certification guidance, study planning, and manager insights.

## Agents

| Agent | Responsibility |
|---|---|
| Orchestrator Agent | Routes the user request to the correct specialist agent |
| Learning Path Curator Agent | Maps role and certification target to required skills and learning content |
| Study Plan Generator Agent | Creates workload-aware study plans for learners |
| Manager Insights Agent | Summarises team readiness, risks, and recommended manager actions |
| Assessment Agent | Planned extension for grounded practice questions |

## Microsoft IQ Integration Plan

This project is designed to integrate with Microsoft Foundry and Foundry IQ.

Foundry IQ will be used as the grounding layer for the synthetic certification guides, workload reports, readiness rules, and learning performance documents.

The local demo currently uses synthetic CSV and markdown files to demonstrate the agent logic. The next step is to connect these documents to a Microsoft Foundry knowledge base and use the Foundry agent workflow for grounded responses.

## Synthetic Data

All data in this repository is synthetic and created only for demonstration. No real employee data, customer data, company data, PII, credentials, or confidential material is included.

## Demo Questions

Try these questions:

1. Give manager readiness insight for TEAM-A
2. Create a study plan for learner L-1001
3. What is the learning path for AZ-204 Cloud Engineer?
4. Show readiness risk for TEAM-B

## How to Run Locally

### 1. Create virtual environment

```bash
python -m venv .venv
```

### 2. Activate virtual environment

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```

### 4. Run CLI demo

```bash
python app/cli.py
```

### 5. Run Streamlit demo

```bash
streamlit run app/streamlit_app.py
```

## Safety and Responsible AI

- Uses synthetic data only.
- Does not include real people, emails, customer data, or company information.
- Does not commit credentials.
- Includes `.env` in `.gitignore`.
- The agent is instructed to say it does not know when the answer is not available from the provided data.

## Architecture

```text
User
 ↓
Orchestrator Agent
 ↓
Specialist Agents
 ├─ Learning Path Curator Agent
 ├─ Study Plan Generator Agent
 └─ Manager Insights Agent
 ↓
Grounded answer using synthetic data and documents
```

## Next Steps

- Connect synthetic documents to Microsoft Foundry / Foundry IQ.
- Add an Assessment Agent for grounded practice questions.
- Add evaluation test cases.
- Record a short demo video.
- Submit the public GitHub repository to the Agents League challenge.
