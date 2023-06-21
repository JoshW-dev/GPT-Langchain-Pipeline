import os
from dotenv import load_dotenv
#load env for OPENAI API Key
from langchain.llms import OpenAI
import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma

load_dotenv()
#split pages from pdf

loader = PyPDFLoader('TSLA_Earnings.pdf')

pages = loader.load_and_split()
# load docs into vector database - ChromaDB
store = Chroma.from_documents(pages, embeddings, collection_name='annualreport')

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY') 

llm =  OpenAI(temperature=0.1)
loader = PyPDFLoader()
prompt = st.text_input("Input your prompt here")

#user hits enter
if prompt:
    response = llm(prompt)
    st.write(response)
    st.text_input=""