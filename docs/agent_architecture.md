# SkillSprint IQ Agent Architecture

SkillSprint IQ is designed as a small multi-agent system for the Reasoning Agents challenge.

## Agents

1. Orchestrator Agent
   - Understands the user's request.
   - Routes the request to the right specialist agent.

2. Learning Path Curator Agent
   - Maps learner role and certification target to skills and learning content.

3. Study Plan Generator Agent
   - Uses certification requirements and workload signals to suggest a realistic study plan.

4. Manager Insights Agent
   - Summarises team readiness, learner risks, and recommended manager actions.

5. Assessment Agent
   - Optional extension.
   - Generates practice questions from approved synthetic certification documents.

## Microsoft IQ Integration Plan

The project will use Microsoft Foundry / Foundry IQ as the grounding layer.
Synthetic markdown documents will be uploaded or indexed as the approved knowledge base.
The agent should cite or clearly reference this knowledge when producing recommendations.

## Safety Design

- Synthetic data only.
- No real employee, customer, company, or confidential data.
- No credentials committed to GitHub.
- Agent should say "I don't know based on the provided data" when information is missing.
