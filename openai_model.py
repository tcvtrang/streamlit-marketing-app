# openai_model.py
import streamlit as st
import openai
import uuid
import time
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
openai.api_key = os.getenv('OPENAI_API_KEY')

def app():
    st.title('OpenAI Model')

    # Initialize OpenAI client
    client = openai

    # Initialize session state variables
    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())

    if "run" not in st.session_state:
        st.session_state.run = {"status": None}

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "retry_error" not in st.session_state:
        st.session_state.retry_error = 0

    if "assistant" not in st.session_state:
        st.session_state.assistant = openai.Completion.create(
            model="text-davinci-003",
            prompt="",
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

    # Vorbereiten des initialen Prompts
    if 'persona_data' in st.session_state and 'company_data' in st.session_state and 'werbespot_data' in st.session_state:
        persona_data = st.session_state['persona_data']
        company_data = st.session_state['company_data']
        werbespot_data = st.session_state['werbespot_data']

        # Erstellen des COMPASS-Prompts
        persona_str = ", ".join([f"{key}: {value}" for key, value in persona_data.items()])
        company_str = ", ".join([f"{key}: {value}" for key, value in company_data.items()])
        werbespot_str = ", ".join([f"{key}: {value}" for key, value in werbespot_data.items()])

        compass_prompt = (
            f"Erstelle ein Werbespot-Skript basierend auf folgenden Informationen:\n\n"
            f"1. User Persona:\n{persona_str}\n\n"
            f"2. Unternehmensinformationen:\n{company_str}\n\n"
            f"3. Werbespot-Details:\n{werbespot_str}\n\n"
            f"COMPASS:\n"
            f"C - Context: Die Werbung ist für das Unternehmen {company_data['unternehmensname']} in der Branche {company_data['branche']}.\n"
            f"O - Objective: Das Ziel der Werbung ist {werbespot_data['ziel_der_werbung']}.\n"
            f"M - Message: Die Hauptbotschaft ist {werbespot_data['handlung_hauptbotschaft']}.\n"
            f"P - Performance: Der Werbespot soll auf dem Kanal {werbespot_data['veröffentlichungskanal']} veröffentlicht werden und die Dauer des Spots beträgt {werbespot_data['laenge']} Sekunden.\n"
            f"A - Audience: Die Zielgruppe des Werbespots umfasst {werbespot_data['zielgruppe']}.\n"
            f"S - Style: Der Ton und Stil des Werbespots ist {werbespot_data['ton_und_stil']}.\n"
            f"S - Scope: Der Call to Action im Werbespot ist {werbespot_data['call_to_action']}.\n"
        )

        st.text_area("COMPASS Prompt", compass_prompt, height=200)

        if st.button("Skript generieren"):
            with st.spinner("Das Skript wird generiert..."):
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=compass_prompt,
                    temperature=0.7,
                    max_tokens=1024,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )

                werbespot_skript = response.choices[0].text.strip()
                st.text_area("Generiertes Werbespot-Skript", werbespot_skript, height=300)
    else:
        st.warning("Bitte geben Sie zuerst Informationen zur User Persona, zum Unternehmen und zum Werbespot ein.")

if __name__ == "__main__":
    app()
