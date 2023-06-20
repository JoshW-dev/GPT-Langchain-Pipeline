import os
from dotenv import load_dotenv

from langchain.llms import OpenAI
import streamlit as st
load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY') 


llm =  OpenAI(temperature=0.1)

prompt = st.text_input("Input your prompt here")

#user hits enter
if prompt:
    response = llm(prompt)
    st.write(response)