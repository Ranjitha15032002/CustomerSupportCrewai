from crewai import Agent
import os
from langchain_openai import ChatOpenAI
from crewai_tools import (
    FileReadTool,
    #DirectoryReadTool,
    SerperDevTool,
    WebsiteSearchTool
)
# Set up environment variables
os.environ["OPENAI_API_KEY"] = "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"
os.environ["SERPER_API_KEY"] = "89baa9de3c1cc66e232da827a76aea24d3092a82"



class CustomAgents:
    def __init__(self):  # Fixed method definition
        # Initialize tools
        self.gpt_model = ChatOpenAI(model_name="gpt-4", temperature=0.7)  # Uncomment if GPT is required
        self.search_tool = SerperDevTool()
        self.web_tool = WebsiteSearchTool()
        #self.knowledge_base_tool = DirectoryReadTool(directory='./knowledge_base')
        self.file_tool = FileReadTool()

    def create_agent(self, role):
        descriptions = {
            "Query Analyzer": "I specialize in analyzing user queries and identifying the core issue.",
            "Problem Solver": "I provide detailed solutions to user queries based on the analysis."
        }

        tools = {
            "Query Analyzer": [self.search_tool, self.web_tool],
            "Problem Solver": [self.file_tool]
        }

        return Agent(
            role=role,
            backstory=descriptions[role],
            goal=f"Efficiently handle {role} tasks to improve customer satisfaction.",
            tools=tools[role],
            verbose=True,
            llm=self.gpt_model  # Uncomment to enable GPT-based responses
        )
