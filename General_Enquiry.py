# GovTech AI Champions Bootcamp Capstone Project
# A ChatBot for Agency for Integrated Care Website

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')


import time
import streamlit as st
from logics.customer_query_handler import process_user_message_general
from helper_functions.utility import check_password
from helper_functions.llm import check_offending_content

if not check_password():
    st.stop()

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="wide",
    page_title="askAIC"
)
# endregion <--------- Streamlit App Configuration --------->

st.title(":blue[askAIC] - Welcome to the :heart: of Care")
with st.expander("Disclaimer", icon=":material/info:"):
    st.markdown("<b>IMPORTANT NOTICE:</b></br>\
            This web application is a prototype developed for educational purposes only.\
            The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.</br></br>\
            <b>Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.</b></br></br>\
            Always consult with qualified professionals for accurate and personalized advice.\
    ", unsafe_allow_html=True)

form = st.form(key="form")
form.subheader("General Enquiry")

user_prompt = form.text_area("Ask me anything related to integrated care", height=100)

if form.form_submit_button("Submit",type="primary"):
    if check_offending_content(user_prompt)=='Yes':
        st.write(":fearful: I am unable to process your request further as I detect inappropriate content such as hate speech or offending expression. Be kind, be caring and be loving for we are the :heart: of Care :innocent:")
    else:    
        with st.spinner('Please wait while we find the answer for you...'):
            time.sleep(5)
            if 'contact' in user_prompt.lower():
                st.write("""The quickest ways to get in touch with AIC are:
                         <ul>
                         <li>To call the AIC Hotline: 1-800-650-6060 (Mon - Fri: 8:30 am - 8:30 pm, Sat: 8:30 am - 4.00 pm)
                         <li>To email AIC at Enquiries@aic.sg
                         </ul>
                         You can also find other ways via this link: https://www.aic.sg/about-us/contact-us-form/')""", unsafe_allow_html=True)
            else:
                user_prompt = user_prompt.replace("AIC","Agency for Integrated Care").replace("A.I.C", "Agency for Integrated Care")
                response = process_user_message_general(user_prompt)
                response = response.replace("```markdown","")
                response = response.replace("```","")
                st.write(response)
