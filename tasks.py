from crewai import Task

class CustomTasks:
    def __init__(self):
        pass

    def create_task(self, agent, task_type, user_query):
      task_descriptions = {
          "query_analysis": f"Analyze the customer's query: {user_query}",
          "problem_resolution": f"Based on the analysis, resolve the customer's issue: {user_query}"
      }

      expected_outputs = {
          "query_analysis": "An identified issue or clarification based on the customer's query.",
          "problem_resolution": "A detailed resolution or next steps for the customer's issue."
      }

      return Task(
          description=task_descriptions[task_type],
          agent=agent,
          expected_output=expected_outputs[task_type]
      )