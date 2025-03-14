from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import os 
import re 



def save_output_to_markdown(task_name: str, output: str, directory: str = "task_outputs"):
    """
    Saves the given output to a Markdown file named after the task.

    Args:
        task_name (str): The name of the task.
        output (str): The output content to save.
        directory (str): The directory where the Markdown file will be saved.
    """
    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)
    
    # Generate a safe filename based on the task name
    safe_task_name = "".join(c if c.isalnum() or c in (' ', '.', '_') else '_' for c in task_name).strip()
    filename = os.path.join(directory, f"{safe_task_name}.md")
    
    # Write the output to the Markdown file
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"# Task: {task_name}\n\n")
        file.write(output)
    
    print(f"✅ Output for '{task_name}' saved as {filename}")


@CrewBase
class SoftwareDevelopmentCrewAutomationLifecycleWorkflowCrew():
    """SoftwareDevelopmentCrewAutomationLifecycleWorkflow crew"""
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def project_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['project_manager'],
            tools=[],
        )

    @agent
    def business_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['business_analyst'],
            tools=[],
        )

    @agent
    def software_architect(self) -> Agent:
        return Agent(
            config=self.agents_config['software_architect'],
            tools=[],
        )

    @agent
    def developer(self) -> Agent:
        return Agent(
            config=self.agents_config['developer'],
            tools=[],
        )

    @agent
    def qa_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['qa_engineer'],
            tools=[],
        )

    @agent
    def technical_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['technical_writer'],
            tools=[],
        )



    @task
    def define_sdlc_roadmap_task(self) -> Task:
        # Initialize the Task object with its configuration
        task_config = self.tasks_config.get('define_sdlc_roadmap_task', {})
        task = Task(
            config=task_config,
            tools=[],
        )

        # # Execute the task to generate the output
        # result = task.run()  # ⬅️ Correct way to execute and retrieve output


        # # Extract the task name from the configuration or use a default name
        # task_name = task_config.get('name', 'define_sdlc_roadmap_task')

        # # Save the output to a text file
        # save_output_to_markdown(task_name, result)

        return task


    @task
    def gather_requirements_task(self) -> Task:
        return Task(
            config=self.tasks_config['gather_requirements_task'],
            tools=[],
        )

    @task
    def architectural_design_task(self) -> Task:
        return Task(
            config=self.tasks_config['architectural_design_task'],
            tools=[],
        )

    @task
    def development_implementation_task(self) -> Task:
        return Task(
            config=self.tasks_config['development_implementation_task'],
            tools=[],
        )

    @task
    def qa_testing_task(self) -> Task:
        return Task(
            config=self.tasks_config['qa_testing_task'],
            tools=[],
        )

    @task
    def documentation_deployment_task(self) -> Task:
        return Task(
            config=self.tasks_config['documentation_deployment_task'],
            tools=[],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the SoftwareDevelopmentCrewAutomationLifecycleWorkflow crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            
            verbose=True,
        )
