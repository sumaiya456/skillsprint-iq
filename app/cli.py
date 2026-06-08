from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from agents import OrchestratorAgent


def main():
    print("SkillSprint IQ - Local Demo")
    print("Ask about TEAM-A readiness, L-1001 study plan, or AZ-204 learning path.")
    print("Type 'exit' to quit.\n")

    orchestrator = OrchestratorAgent()

    while True:
        question = input("You: ").strip()
        if question.lower() in {"exit", "quit"}:
            break
        response = orchestrator.route(question)
        print(f"\n[{response.agent_name}]")
        print(response.answer)
        print()


if __name__ == "__main__":
    main()
