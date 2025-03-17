import asyncio
import chainlit as cl
from chainlit.input_widget import TextInput
from crewai import Agent, Task, Crew
import json

# Sample SDLC agents
from software_development_crew_automation_lifecycle_workflow.crew import SoftwareDevelopmentCrewAutomationLifecycleWorkflowCrew
 # Import your crew

@cl.on_chat_start
async def start():
    # Define the input widgets
    inputs = [
        TextInput(id="project_idea", label="Project Idea", placeholder="e.g., AI Email Responder"),
        TextInput(id="dev_platform", label="Development Platform", placeholder="e.g., Python, CrewAI"),
        TextInput(id="prod_deployment_platform", label="Deployment Platform", placeholder="e.g., AWS, CrewAI Enterprise"),
        TextInput(id="project_stack", label="Tech Stack", placeholder="e.g., CrewAI, Flask, Django"),
        TextInput(id="requirements_specification", label="Requirements Specification", placeholder="Describe features"),
        TextInput(id="technical_constraints", label="Technical Constraints", placeholder="e.g., API limits"),
        TextInput(id="testing_criteria", label="Testing Criteria", placeholder="Describe validation criteria"),
    ]

    # Send a message requesting user input
    ask_message = cl.AskUserMessage(
        content="Please provide the following details:"
    )
    user_response = await ask_message.send()


    # Process the user inputs
    await handle_user_inputs(user_response)

async def handle_user_inputs(user_response):
    if not user_response:
        await cl.Message(content="⚠️ No input received! Please try again.").send()
        return

    # Extract the inputs
    project_idea = user_response.get("project_idea")
    dev_platform = user_response.get("dev_platform")
    # Extract other inputs as needed...

    # Run the CrewAI SDLC workflow
    crew_instance = SoftwareDevelopmentCrewAutomationLifecycleWorkflowCrew()
    if crew_instance:
        results = crew_instance.crew().kickoff(inputs=user_response)

        response = "**✅ SDLC Workflow Results:**\n\n"
        for task_output in results.tasks_output:
            if task_output:
                response += f"### 🛠 {task_output.name}\n"
                response += f"```python\n{task_output.raw[:500]}...\n```\n\n"

        await cl.Message(content=response).send()
    else:
        await cl.Message(content="🚀 CrewAI instance is not initialized!").send()
        
# Run the start function
if __name__ == "__main__":
    asyncio.run(start())
