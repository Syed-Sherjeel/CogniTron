from crewai import Crew 

from task import plan, write, edit
from agents import planner, writer, editor

crew = Crew(
   agents=[planner, writer, editor],
   tasks=[plan, write, edit],
   verbose=2 
)