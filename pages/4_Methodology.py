import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    page_title="askAIC",
    layout="wide"
    
)
# endregion <--------- Streamlit App Configuration --------->

st.title(":blue[askAIC] - Methodology")

st.subheader("File Structure")
st.markdown("""Root</br>
            <ul>
            <li>General_Enquiry.py
            <li>helper_functions
                <ul>
                <li>llm.py
                <li>utility.py
                </ul>
            <li>logics
                <ul>
                <li>customer_query_handler.py
                </ul>
            <li>pages
                <ul>
                <li>2_Financial_Assistance.py
                <li>3_About_Us.py
                <li>4_Methodology.py
                </ul>
            </ul>
            """,\
            unsafe_allow_html=True)

st.subheader("Flowcharts")
with st.expander("Flowchart for General Enquiry (click to expand or collapse)"):
    st.image("General Enquiry Flowchart.png")

with st.expander("Flowchart for Financial Assistance (click to expand or collapse)"):   
    st.image("Financial Assistance Flowchart.png")