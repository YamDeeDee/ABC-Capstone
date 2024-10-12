import os
from openai import OpenAI
import streamlit as st

# Pass the API Key to the OpenAI Client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# This is the "Updated" helper function for calling LLM
def get_completion(prompt, model="gpt-4o-mini", temperature=0, top_p=1.0, max_tokens=1024, n=1, json_output=False):
    if json_output == True:
      output_json_structure = {"type": "json_object"}
    else:
      output_json_structure = None

    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create( #originally was openai.chat.completions
        model=model,
        messages=messages,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
        n=1,
        response_format=output_json_structure,
    )
    return response.choices[0].message.content

def check_offending_content(content):
    print("Checking offending comment")
    prompt = f"""
    Do you think {content} contains 'Hate Speech' or is 'Offending' in nature? 
    The definition of hate speech is a speech that attacks a person or group on the basis of attributes such as race, religion, ethnic origin, national origin, sex, disability, sexual orientation,
    or gender identity. The content is 'Offending' if it 
    1. suggests actions that are illegal in the eyes of law or considered unethical or
    2. cause harm or any form of discomfort including anger, distress and embarrassment or
    3. contains derogatory words or expressions or
    4. contains disrespectful words or expressions
    Only answer with a 'Yes' or 'No'"""
    result = get_completion(prompt)
    print(result)
    return result

