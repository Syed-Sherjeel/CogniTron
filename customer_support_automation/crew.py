from crewai import Crew

from task import quality_assurance_review, inquiry_resolution
from agents import support_quality_assurance_agent, support_agent


crew =  Crew(
    tasks=[inquiry_resolution, quality_assurance_review],
    agents=[support_agent, support_quality_assurance_agent],
    verbose=2,
    #memory=True
)

