#!/usr/bin/env python
import sys
from software_development_crew_automation_lifecycle_workflow.crew import SoftwareDevelopmentCrewAutomationLifecycleWorkflowCrew
from .crew import save_output_to_markdown
# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information
def run():
    """
    Run the AI Email Responder Crew with structured test inputs.
    """
    inputs = {
        'project_idea': 'Automated AI Email Responder', #Automated AI Email Responder
        'dev_platform': 'Python + CrewAI + chainlit',
        'prod_deployment_platform': 'crewai enterprise',
        'project_stack': 'CrewAI, Flask, IMAP/SMTP, Google gemiini API, chainlit, django',
        'requirements_specification': 'Fetch new emails, analyze, and auto-generate responses.',
        'technical_constraints': 'Limited API requests per day.',
        'testing_criteria': 'Ensure accurate response generation & email parsing.',
        'documentation_format': 'Markdown (README.md), or Filename ({filename}.py)'
    }
# Initialize the crew
    crew_instance = SoftwareDevelopmentCrewAutomationLifecycleWorkflowCrew()
# Run the crew and capture task results
    results = crew_instance.crew().kickoff(inputs=inputs)

# Iterate over task results and save outputs
    for index, task_output in enumerate(results.tasks_output):
        if task_output:
            # Extract the task name from the task output
            task_name = task_output.name
            
            # Save the output to a Markdown file
            save_output_to_markdown(task_name, task_output.raw)
        else:
            print("Output not captured from results")

    print("✅ All task outputs saved successfully!")

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'project_idea': 'sample_value',
        'dev_platform': 'sample_value',
        'prod_deployment_platform': 'sample_value',
        'project_stack': 'sample_value',
        'requirements_specification': 'sample_value',
        'technical_constraints': 'sample_value',
        'testing_criteria': 'sample_value',
        'documentation_format': 'sample_value'
    }
    try:
        SoftwareDevelopmentCrewAutomationLifecycleWorkflowCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        SoftwareDevelopmentCrewAutomationLifecycleWorkflowCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'project_idea': 'sample_value',
        'dev_platform': 'sample_value',
        'prod_deployment_platform': 'sample_value',
        'project_stack': 'sample_value',
        'requirements_specification': 'sample_value',
        'technical_constraints': 'sample_value',
        'testing_criteria': 'sample_value',
        'documentation_format': 'sample_value'
    }
    try:
        SoftwareDevelopmentCrewAutomationLifecycleWorkflowCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
