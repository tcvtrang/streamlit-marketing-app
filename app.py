 # Importing required packages
import streamlit as st
import Werbespot
import user_persona
import company_info
import openai_model
import data
# import test123
# import music_generator

# To use this app, you need an .env file with the OPENAI API
# and you need to fill in the ID in the assistant.py file

PAGES = {
    "Werbespot": Werbespot,
    "User Persona": user_persona,
    "Company Information": company_info,
    "Data": data,
    "OpenAI Model": openai_model,
    # "Test123": test123,
    # "Music Generator": music_generator
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page.app()