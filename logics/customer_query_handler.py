from crewai import Agent, Task, Crew
from crewai_tools import WebsiteSearchTool
from IPython.display import display, Markdown
import streamlit as st


OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

# depending on the use case, use the appropriate backstory and task description for the different agents

# General Enquiry
planner_backstory_general = """You're working on planning a response to a query: {query}.
        Any reference to 'AIC' in {query} should be replaced by 'Agency for Integrated Care'.
        You collect information that helps the audience obtain the relevant answers to their queries.
        Your work is the basis for the Content Writer to write a response to this query.
        Use only the tools provided to gather the information.
        The information you provide should only be from 'https://www.aic.sg/'.
        """

writer_backstory_general = """You're working on writing the response to the query: {query}.
        You base your writing on the work of the Content Planner, who provides an outline and relevant context about the query.
        You follow the main objectives and direction of the outline as provide by the Content Planner."""

#1. Identify the target audience, considering their interests and pain points.

planner_task_description_general = """\
        1. Only use information from https://www.aic.sg.
        2. Develop a detailed content outline, including key points.
        3. Respond with 'No relevant information' if you are not able to find relevant information linking {query} to 'Agency for Integrated Care'."""

writer_task_description_general = """\
        1. Use the content plan to craft a response on {query} based on the target audience's interests.
        2. Only use information from https://www.aic.sg.
        3. Do not provide email addresses and phone numbers other than those obtained from https://www.aic.sg.
        3. If the response from Content Planner contains 'No relevant information', respond with 'No answer'
        4. Proofread for grammatical errors."""

# Financial Assistance

planner_backstory_financial = """You're working on gathering information to answer to the query: {query}.
        Use only the tools provided to gather the information.
        The information you provide should only be from 'https://www.aic.sg/financial-assistance/'.
        Your work is the basis for the Content Writer to write a response to this query.
        """

writer_backstory_financial = """You're working on writing the response to the query: {query}.
        You base your writing on the work of the Content Planner, who provides the information that you will use.
        """

planner_task_description_financial = """\
        1. Only use information from 'https://www.aic.sg/financial-assistance/'.
        3. Provide your information as a list of items with a description for each item."""

writer_task_description_financial = """\
        1. Use the content plan to craft a response on {query} based on the target audience's interests.
        2. Only use information from 'https://www.aic.sg/financial-assistance/'.
        3. Output your response in a table consisting of two columns with the following columns names:
            'Financial Assistance Scheme' - title of the financial assistance scheme
            'Description' - description of the financial assistance scheme, including eligibility criteria if any
        4. There is no need to include conclusion in your output.
        5. End your response with "For more details on financial assistance schemes, you can visit https://www.aic.sg/financial-assistance".
        6. Proofread for grammatical errors."""

def createCrew(pb, pt, wb, wt, url):

    # pb - planner_backstory
    # pt - planner_task_description
    # wb - writer_backstory
    # wt - write_task_description

    tool_websearch = WebsiteSearchTool(url)

    # Creating Agents
    agent_planner = Agent(
        role="Content Planner",
        goal="Gather and plan engaging and factually accurate content on {query}",
        max_iter="10",
        backstory = pb,
        tools=[tool_websearch],
        allow_delegation=False, 
        verbose=True, 
    )

    agent_writer = writer = Agent(
        role="Content Writer",
        goal="Write factually accurate response to the query: {query}",
        max_iter="10",
        backstory = wb,
        allow_delegation=False, 
        verbose=True, 
    )

    # Creating Tasks
    task_plan = Task(
        description = pt,
        expected_output="""\
        A comprehensive content plan document with an outline and key points""",
        agent=agent_planner,
    )

    task_write = Task(
        description = wt,
        expected_output="""
        A well-written response "in markdown format.""",
        agent=agent_writer,
    )

    # Creating the crew
    crew = Crew(
        agents=[agent_planner, agent_writer],
        tasks=[task_plan, task_write],
        verbose=False
    )

    return crew

def process_user_message_general(user_input):
    crew = createCrew(planner_backstory_general, planner_task_description_general, writer_backstory_general, writer_task_description_general, "https://www.aic.sg/")
    result = crew.kickoff(inputs={"query": user_input})
    print(result.tasks_output[0])
    return result.raw

def process_user_message_financial(user_input):
    crew = createCrew(planner_backstory_financial, planner_task_description_financial, writer_backstory_financial, writer_task_description_financial, "https://www.aic.sg/financial-assistance/")
    result = crew.kickoff(inputs={"query": user_input})
    print(result.tasks_output[0])
    return result.raw