#!/usr/bin/env python
import os
import PyPDF2
import warnings
from dotenv import load_dotenv
from datetime import datetime
from crewai import Crew, Agent, Task
from textwrap import dedent
import yaml

# Load environment variables first
load_dotenv()

# Remove the hardcoded API key - it will be loaded from .env
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs',
        'current_year': str(datetime.now().year)
    }
    
    try:
        Resumebuild().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Resumebuild().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Resumebuild().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Resumebuild().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

# Load configurations
def load_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Load agents and tasks configurations
agents_config = load_config('src/resumebuild/config/agents.yaml')
tasks_config = load_config('src/resumebuild/config/tasks.yaml')

def read_pdf(pdf_path):
    """Read PDF content"""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Move this function outside of create_resume_crew
def save_updated_resume(result, resume_path):
    if "UPDATED_RESUME:" in result:
        updated_content = result.split("UPDATED_RESUME:")[1].strip()
        output_path = os.path.join(
            os.path.dirname(resume_path),
            'updated_resume.txt'
        )
        with open(output_path, 'w') as f:
            f.write(updated_content)
        print(f"\nUpdated resume saved to: {output_path}")

def create_resume_crew(resume_path, job_posting_path):
    # Read resume and job posting content
    resume_content = read_pdf(resume_path)
    with open(job_posting_path, 'r') as file:
        job_posting = file.read()

    # Create agents
    analyzer = Agent(
        name=agents_config['resume_analyzer']['name'],
        role=agents_config['resume_analyzer']['role'],
        goal=agents_config['resume_analyzer']['goals'][0],
        backstory=agents_config['resume_analyzer']['backstory'],
        verbose=True
    )

    editor = Agent(
        name=agents_config['resume_editor']['name'],
        role=agents_config['resume_editor']['role'],
        goal=agents_config['resume_editor']['goals'][0],
        backstory=agents_config['resume_editor']['backstory'],
        verbose=True
    )

    reviewer = Agent(
        name=agents_config['resume_reviewer']['name'],
        role=agents_config['resume_reviewer']['role'],
        goal=agents_config['resume_reviewer']['goals'][0],
        backstory=agents_config['resume_reviewer']['backstory'],
        verbose=True
    )

    # Create tasks with actual content
    analyze = Task(
        description=f"""
        Analyze this resume content:
        {resume_content}
        
        For this job posting:
        {job_posting}
        
        Identify gaps and opportunities for improvement.
        """,
        expected_output=tasks_config['analyze_resume']['expected_output'],
        agent=analyzer
    )

    edit = Task(
        description=f"""
        Based on the analysis, update this resume content:
        {resume_content}
        
        To better match this job posting:
        {job_posting}
        
        Provide the complete updated resume content in a clear format that can be saved to a file.
        Start your response with "UPDATED_RESUME:" followed by the new content.
        """,
        expected_output=tasks_config['edit_resume']['expected_output'],
        agent=editor
    )

    review = Task(
        description="Review the updated resume for quality and optimization",
        expected_output=tasks_config['review_resume']['expected_output'],
        agent=reviewer
    )

    # Create and return the crew
    crew = Crew(
        agents=[analyzer, editor, reviewer],
        tasks=[analyze, edit, review],
        verbose=True
    )

    return crew

def main():
    # Paths to your resume and job posting
    resume_path = "C:\\Users\\shrey\\OneDrive\\Desktop\\resume.pdf"
    job_posting_path = "C:\\Users\\shrey\\OneDrive\\Desktop\\job_posting.txt"
    
    # Verify files exist
    if not os.path.exists(resume_path):
        print(f"Error: Resume file not found at {resume_path}")
        return
    
    if not os.path.exists(job_posting_path):
        print(f"Error: Job posting file not found at {job_posting_path}")
        return
        
    # Print file contents to verify
    print("\nJob Posting Contents:")
    with open(job_posting_path, 'r') as f:
        print(f.read())
        
    print("\nResume file exists:", os.path.exists(resume_path))
    
    # Create and run the crew
    crew = create_resume_crew(resume_path, job_posting_path)
    result = crew.kickoff()
    
    # Save the updated resume
    save_updated_resume(result, resume_path)  # Pass resume_path as argument
    
    print("\nFinal Result:")
    print(result)

if __name__ == "__main__":
    main()
