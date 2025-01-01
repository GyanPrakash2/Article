from crewai import Crew, Process
from agents import planner, writer, editor, converter
from tasks import plan, write, edit, convert_to_pdf

crew = Crew(
    agents=[planner, writer, editor, converter],
    tasks=[plan, write, edit, convert_to_pdf],
    verbose=True,
    process=Process.sequential,
)

result = crew.kickoff(inputs={"topic": "Artificial Intelligence"})