import streamlit as st
from logics.customer_query_handler import process_user_message_financial

st.set_page_config(
    page_title="askAIC",
    layout="wide"
    
)

st.title(":blue[askAIC] - Welcome to the :heart: of Care")

with st.expander("Disclaimer", icon=":material/info:"):
    st.markdown("<b>IMPORTANT NOTICE:</b></br>\
            This web application is a prototype developed for educational purposes only.\
            The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.</br></br>\
            <b>Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.</b></br></br>\
            Always consult with qualified professionals for accurate and personalized advice.\
    ", unsafe_allow_html=True)

st.subheader("Financial Assistance")

genre = st.radio(
    "AIC provides information on a range of financial assistance to support different needs. Select one of the needs below and click on the 'Submit' button:",
    ["Everyday Needs", "Medical Bills", "Support for Caregivers"],
    captions=[
        "From daily costs of living to medical fees",
        "Easing healthcare cost, so that you and your loved one can focus on rest and recovery",
        "Financial support for your caregiving needs",
    ],
)

if st.button("Submit", type="primary"):
    with st.spinner('Please wait while we gather the information for you...'):
        user_prompt = "Tell me about Financial Assistance schemes related to '" + genre + "' in https://www.aic.sg/financial-assistance/"
        response = process_user_message_financial(user_prompt)
        response = response.replace("```markdown","").replace("```","").replace("$","\$")
        st.write("Here are the information related to Financial Assistance schemes for <b>" + genre + "</b>", unsafe_allow_html=True)
        st.write(response)

