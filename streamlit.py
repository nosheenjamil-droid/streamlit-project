from google import genai
from google.genai import types
from google.genai import errors
from dotenv import load_dotenv
import os
load_dotenv()

client = genai.Client(api_key="GOOGLE_GEMINI_API_KEY")

import streamlit as st
st.title("hello stremlit!")
st.write("this is a simple streamlit app.")
st.slider("select a value",0,100,50)
st.button("click me!")
st.subheader("Chatbot form")
user_input = st.text_input("enter your query:")
if st.button("Submit"):
    response = client.models.generate_content(
        model="gemini-3.5-flash",contents= user_input
    )
    st.write(response.text)

