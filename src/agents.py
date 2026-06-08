from dataclasses import dataclass
from pathlib import Path
import pandas as pd


DATA_DIR = Path(__file__).resolve().parents[1] / "data"


@dataclass
class AgentResponse:
    agent_name: str
    answer: str


class LearningPathCuratorAgent:
    name = "Learning Path Curator Agent"

    def run(self, role: str, certification: str) -> AgentResponse:
        certs = pd.read_csv(DATA_DIR / "certification_requirements.csv")
        match = certs[(certs["primary_role"].str.lower() == role.lower()) & (certs["certification"].str.lower() == certification.lower())]

        if match.empty:
            return AgentResponse(self.name, "I don't know based on the provided synthetic certification data.")

        row = match.iloc[0]
        skills = row["skills"].split("; ")
        answer = (
            f"For a {role} preparing for {certification}, the recommended learning path should cover: "
            + ", ".join(skills)
            + f". Recommended study hours: {row['recommended_hours']}. Target practice score: {row['target_practice_score']}%."
        )
        return AgentResponse(self.name, answer)


class StudyPlanGeneratorAgent:
    name = "Study Plan Generator Agent"

    def run(self, learner_id: str) -> AgentResponse:
        learners = pd.read_csv(DATA_DIR / "learners.csv")
        workload = pd.read_csv(DATA_DIR / "workload_signals.csv")
        certs = pd.read_csv(DATA_DIR / "certification_requirements.csv")

        learner = learners[learners["learner_id"] == learner_id]
        if learner.empty:
            return AgentResponse(self.name, "I don't know based on the provided synthetic learner data.")

        learner_row = learner.iloc[0]
        workload_row = workload[workload["learner_id"] == learner_id].iloc[0]
        cert_row = certs[certs["certification"] == learner_row["certification"]].iloc[0]

        remaining_hours = max(0, int(cert_row["recommended_hours"]) - int(learner_row["hours_studied"]))
        meeting_hours = int(workload_row["meeting_hours_per_week"])
        focus_hours = int(workload_row["focus_hours_per_week"])

        if meeting_hours > 20 or focus_hours < 12:
            weekly_hours = 3
            pacing_note = "Use a lighter plan because workload pressure is high."
        else:
            weekly_hours = 5
            pacing_note = "Use a normal focused study plan."

        weeks_needed = max(1, -(-remaining_hours // weekly_hours)) if remaining_hours else 1

        answer = (
            f"Learner {learner_id} is preparing for {learner_row['certification']}. "
            f"Remaining recommended study hours: {remaining_hours}. "
            f"Suggested weekly study load: {weekly_hours} hours for about {weeks_needed} week(s). "
            f"Preferred learning slot: {workload_row['preferred_learning_slot']}. {pacing_note}"
        )
        return AgentResponse(self.name, answer)


class ManagerInsightsAgent:
    name = "Manager Insights Agent"

    def run(self, team_id: str) -> AgentResponse:
        learners = pd.read_csv(DATA_DIR / "learners.csv")
        workload = pd.read_csv(DATA_DIR / "workload_signals.csv")

        team = learners[learners["team_id"] == team_id]
        if team.empty:
            return AgentResponse(self.name, "I don't know based on the provided synthetic team data.")

        merged = team.merge(workload, on=["learner_id", "team_id"], how="left")
        at_risk = merged[merged["status"] == "At Risk"]
        ready = merged[merged["status"] == "Ready"]

        risk_lines = []
        for _, row in at_risk.iterrows():
            reason = []
            if int(row["practice_score_avg"]) < 70:
                reason.append("low practice score")
            if int(row["meeting_hours_per_week"]) > 20:
                reason.append("high meeting load")
            if int(row["focus_hours_per_week"]) < 12:
                reason.append("low focus hours")
            risk_lines.append(f"{row['learner_id']} ({row['role']}, {row['certification']}): {', '.join(reason)}")

        if risk_lines:
            action = "Recommended manager action: review workload, protect focus time, and schedule a checkpoint assessment."
        else:
            action = "Recommended manager action: keep current plan and schedule final mock assessments."

        answer = (
            f"{team_id} readiness summary: {len(ready)} ready learner(s), {len(at_risk)} at-risk learner(s). "
            f"Risk details: {'; '.join(risk_lines) if risk_lines else 'No major risk detected.'} "
            f"{action}"
        )
        return AgentResponse(self.name, answer)


class OrchestratorAgent:
    name = "Orchestrator Agent"

    def __init__(self):
        self.learning_agent = LearningPathCuratorAgent()
        self.study_agent = StudyPlanGeneratorAgent()
        self.manager_agent = ManagerInsightsAgent()

    def route(self, question: str) -> AgentResponse:
        q = question.lower()

        if "team" in q or "manager" in q or "risk" in q or "readiness" in q:
            # simple demo routing
            team_id = "TEAM-A"
            for possible_team in ["TEAM-A", "TEAM-B", "TEAM-C"]:
                if possible_team.lower() in q:
                    team_id = possible_team
            return self.manager_agent.run(team_id)

        if "study plan" in q or "learner" in q or "schedule" in q:
            learner_id = "L-1001"
            for possible_learner in ["L-1001", "L-1002", "L-1003", "L-1004", "L-1005"]:
                if possible_learner.lower() in q:
                    learner_id = possible_learner
            return self.study_agent.run(learner_id)

        if "learning path" in q or "certification" in q or "skills" in q:
            if "az-400" in q or "devops" in q:
                return self.learning_agent.run("DevOps Engineer", "AZ-400")
            if "dp-203" in q or "data engineer" in q:
                return self.learning_agent.run("Data Engineer", "DP-203")
            if "ai-102" in q or "ai engineer" in q:
                return self.learning_agent.run("AI Engineer", "AI-102")
            return self.learning_agent.run("Cloud Engineer", "AZ-204")

        return AgentResponse(self.name, "I don't know based on the provided synthetic data. Try asking about a team, learner, study plan, or certification.")
