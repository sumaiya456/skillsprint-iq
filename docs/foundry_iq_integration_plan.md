# Foundry IQ Integration Plan

## Purpose

SkillSprint IQ is designed for the Agents League Reasoning Agents challenge as a multi-agent certification readiness assistant.

The current version runs locally using synthetic CSV and markdown files. The planned Microsoft IQ integration is to use Microsoft Foundry and Foundry IQ as the grounding layer for the agent knowledge base.

## Why Foundry IQ

Foundry IQ is the best fit for this project because the agent needs to retrieve approved learning content, readiness rules, workload guidance, and certification requirements from trusted documents.

In this project, Foundry IQ would ground the agent responses using synthetic documents only.

## Knowledge Sources

The following synthetic documents are prepared for Foundry IQ ingestion:

- `docs/engineering_certification_guide.md`
- `docs/team_learning_report.md`
- `docs/workload_insights_report.md`
- `docs/readiness_rules.md`

These documents represent approved enterprise learning guidance, workload patterns, and certification readiness rules.

## Synthetic Structured Data

The following synthetic CSV files support the local reasoning demo:

- `data/learners.csv`
- `data/workload_signals.csv`
- `data/certification_requirements.csv`
- `data/learner_progress.csv`

These files use fictional learner IDs, team IDs, roles, certifications, practice scores, and workload signals.

## Planned Foundry IQ Flow

```text
User question
   ↓
Orchestrator Agent
   ↓
Specialist Agent
   ↓
Foundry IQ Knowledge Base
   ↓
Grounded answer with reasoning