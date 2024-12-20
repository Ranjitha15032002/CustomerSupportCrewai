import os
from crewai import Crew
from crewai.process import Process
from agents import CustomAgents
from tasks import CustomTasks
import logging


logging.basicConfig(level=logging.DEBUG)


class CustomerSupport:
    def __init__(self):
        self.agents = CustomAgents()
        self.tasks = CustomTasks()
        logging.debug("Customer Support System initialized.")

    def handle_query(self, user_query):
    # Define agents
      agents = {
          "query_analyzer": self.agents.create_agent("Query Analyzer"),
          "problem_solver": self.agents.create_agent("Problem Solver")
      }

      # Assign tasks with user query passed as context
      tasks = {
          "analysis": self.tasks.create_task(agents["query_analyzer"], "query_analysis", user_query),
          "resolution": self.tasks.create_task(agents["problem_solver"], "problem_resolution", user_query)
      }

      # Create a Crew instance
      crew = Crew(
          agents=list(agents.values()),
          tasks=list(tasks.values()),
          verbose=True,
          process=Process.hierarchical,
          memory=True,
          planning=True  # Enable verbose for debugging
                  )

      # Pass user query in a dictionary for interpolation
      logging.debug("Crew initialized. Starting task execution.")
      input_data = {"user_query": user_query}
      return crew.kickoff(input_data)



if __name__ == "_main_":
    print("Welcome to the Customer Support System")
    print("---------------------------------------")
    user_query = input("Please enter your query: ").strip()
    try:
        support_system = CustomerSupport()
        result = support_system.handle_query(user_query)
        print("\n\n########################")
        print("## Resolution to your query:")
        print("########################\n")
        print(result)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print(f"Error: {e}")
    