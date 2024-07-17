from crewai import Task

from agents import support_agent, support_quality_assurance_agent
from tools import docs_scrape_tool



inquiry_resolution = Task(
    description="{customer} reached out with a super important ask:\n"
                 "{inquiry}\n\n"
                 "{person} from {customer} is the one that reached out. "
                 "Make sure to use everything you know "
                 "to provide the best support possible " 
                 "You must strive to provide complete and accurate response to customer's inquiry",
    expected_output="A detailed, informative response to the "
                     "customer's inquiry that addresses "
                     "all aspect of their question. \n "
                     "The response should include references "
                     "to everything you used to find answers "
                     "including external data or solutions. "
                     "Ensure answer is complete, "
                     "leaving no questions unanswered, and maintain a helpful and friendly "
                     "tone throughout ",
    tools=[docs_scrape_tool],
    agent=support_agent
    
)

quality_assurance_review = Task(
    description="Review the response drafted by Senior Support Representatives for {customer}'s inquiry"
                 "Ensure answer is comprehensive, accurate and adheres to "
                 "the high quality standards expected for customer support \n"
                 "Verify all parts of customer's inquiry have been addressed "
                 "thoroughly, with a helpful and friendly tone.\n "
                 "Check for references and sources used to find the infromation, "
                 "ensuring the answer is well supported and leaves no questions unanswered.",
    expected_output="A final, detailed and informative response "
                     "ready to be sent to the customer\n"
                     "This response should fully address the customer's inquiry, incorporating "
                     "all relevant feedback and improvements.\n"
                     "Don't be formal we are chill and cool company "
                     "but main a friendly and professional tone throughout",
    agent=support_quality_assurance_agent
)
