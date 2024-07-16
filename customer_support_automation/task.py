from crewai_tools import SerperDevTool, \
                        ScrapeElementFromWebsiteTool, \
                        ScrapeElementFromWebsiteTool
                        

docs_scrape_tool = ScrapeElementFromWebsiteTool(
    website_url="https://docs.crewai.com/how-to/Creating-a-Crew-and-kick-it-off/"
)

