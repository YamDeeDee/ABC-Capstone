import streamlit as st

st.set_page_config(
    page_title="askAIC",
    layout="wide"
    
)

st.sidebar.image(["Female Caregiver.jpeg","Male Caregiver.jpeg","Senior Citizens.jpg"],width=94)
st.sidebar.caption("***Pictures AI-generated. Any resemblance to person(s) is purely coincidental.***")
st.sidebar.caption("***Submitted By:*** HANG Kim  Yam")

st.title("ask:blue[AIC] - Welcome to the :heart: of Care")
st.markdown("""***an LLM-powered web-application developed in partial fulfillment of the Singapore GovTech AI Champions Bootcamp 2024***""")

st.subheader(":blue[Project Objectives]")
st.markdown("""To develop a web-application that enables users to</br>
            <ul>
            <li>make <b>General Enquiries</b> related to the Singapore Agency for Integrated Care (AIC), using natural language
            <li>obtain quick summary of <b>Financial Assistance</b> schemes based on different category of needs
            </ul>
            This application aims to be a convenient 'first-stop' for users wishing to get information related to integrated care based on a topic of their interest. 
            We hope the relative simplicity with which this application is developed will also lend itself to be easily adapted for use for other websites.</br></br>
            :blue[***About AIC***]</br>
            The Agency for Integrated Care (AIC) was established in 1992 as the Care Liaison Services (CLS) under the Ministry of Health to coordinate and facilitate the placement of elderly sick to nursing homes and chronic sick units. 
            AIC today is the designated single agency to coordinate the delivery of aged care services, and to enhance service development and capability-building across both the health and social domain. 
            It works closely with Community Care partners in supporting them in service development and manpower-capability building to raise the quality of care and bringing care support closer to those in need.</br>
            ***Source***: https://www.aic.sg/about-us/
            """,\
            unsafe_allow_html=True)
st.subheader(":blue[Project Scope]")
st.markdown("""The project involves the development of</br>
            <ul>
                <li>front-end user interface using Streamlit for the following web pages:
                <ul>
                    <li>General Enquiry
                    <li>Financial Assistance
                    <li>About Us
                    <li>Methodology
                </ul>\
                <li>back-end logic to process and respond to user inputs
            </ul>""", unsafe_allow_html=True)
st.subheader(":blue[Data Sources]")
st.markdown("""<ul>
                <li>Official website of Agency for Integrate Care (https://www.aic.sg/)
                <li>OpenAI LLM GPT-4o-mini
            </ul>""",
            unsafe_allow_html=True)
st.subheader(":blue[Project Features]")
st.markdown("""On the <b>front-end</b>, the application focus on presenting a clean and simple interface where users need at most two clicks to get information.</br>
            On the <b>back-end</b> where CrewAI agents are deployed with WebSearchTool to search specific websites and being mindful that we do not want the target websites to be searched using inappropriate keywords or expressions, an additional layer is introduced to check for inappropriate content in the user prompt before deploying agents to complete the tasks.""",unsafe_allow_html=True)
st.subheader(":blue[Acknowlegement]")
st.markdown("""This project would not have been possible without the influence of a number of people:</br>
            <ul>
                <li>Dr. Nick Tan, Senior Data Scientist @ GovTech & Instructor for the AI Champions Bootcamp 2024 - for the vast amount of knowledge that he patiently imparted to us in the course, incredibly, in 8 weeks
                <li>Fellow learners from various government agencies for the discussion during synchronous online lessons and tips shared on the discussion forum 
                <li>My colleagues who are on this program together with me
            </ul>
            """,unsafe_allow_html=True)
