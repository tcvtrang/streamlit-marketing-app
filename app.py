 # Importing required packages
import streamlit as st
import Willkommen
import company_info
import Werbespot
import user_persona
import openai_model
import data
import Sonstiges
# import test123
# import music_generator

# To use this app, you need an .env file with the OPENAI API
# and you need to fill in the ID in the assistant.py file

PAGES = {
    "Willkommen": Willkommen,
    "Unternehmensninformationen": company_info,
    "Informationen zur Erstellung des Werbespot-Skripts": Werbespot,
    "Persona der Zielgruppe": user_persona,
    "Sonstiges": Sonstiges,
    "Data": data,
    "OpenAI Model": openai_model,
    # "Test123": test123,
    # "Music Generator": music_generator
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page.app()