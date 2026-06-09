import sys
from pathlib import Path
import streamlit as st
import pandas as pd

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))
from agents import OrchestratorAgent

BASE_DIR = Path(__file__).resolve().parents[1]

st.set_page_config(page_title="SkillSprint IQ", page_icon="🧠")

st.title("SkillSprint IQ")
st.write("A synthetic multi-agent certification readiness assistant for enterprise learning teams.")

st.warning("Demo safety note: This app uses synthetic data only. No real employee, customer, company, or confidential data is included.")

question = st.text_input(
    "Ask SkillSprint IQ",
    value="",
    placeholder="Type your own question or choose one below"
)

examples = [
    "Give manager readiness insight for TEAM-A",
    "Create a study plan for learner L-1001",
    "What is the learning path for AZ-204 Cloud Engineer?",
    "Generate practice assessment for learner L-1001",
    "Show readiness risk for TEAM-B",
]

selected = st.selectbox("Or choose a demo question", examples)

if st.button("Run Agent"):
    orchestrator = OrchestratorAgent()
    response = orchestrator.route(question or selected)
    st.subheader(response.agent_name)
    st.write(response.answer)

st.divider()
st.subheader("Synthetic Learner Data")
st.dataframe(pd.read_csv(BASE_DIR / "data" / "learners.csv"))

st.subheader("Synthetic Workload Signals")
st.dataframe(pd.read_csv(BASE_DIR / "data" / "workload_signals.csv"))
