 # Importing required packages
import streamlit as st
import openai
import uuid
import time
from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
from assistant import OPENAI_ASSISTANT


def app():
    st.title('OpenAI Model')

    # Initialize OpenAI client
    client = OpenAI()


    # Initialize session state variables
    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())

    if "run" not in st.session_state:
        st.session_state.run = {"status": None}

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "retry_error" not in st.session_state:
        st.session_state.retry_error = 0


# Initialize OpenAI assistant
    if "assistant" not in st.session_state:
        openai.api_key = os.getenv('OPENAI_API_KEY')
        st.session_state.assistant = openai.beta.assistants.retrieve(OPENAI_ASSISTANT)
        st.session_state.thread = client.beta.threads.create(
            metadata={'session_id': st.session_state.session_id}
     )

# Display chat messages
    elif hasattr(st.session_state.run, 'status') and st.session_state.run.status == "completed":
        st.session_state.messages = client.beta.threads.messages.list(
            thread_id=st.session_state.thread.id
     )
        for message in reversed(st.session_state.messages.data):
            if message.role in ["user", "assistant"]:
                with st.chat_message(message.role):
                    for content_part in message.content:
                        message_text = content_part.text.value
                        st.markdown(message_text)


# Vorbereiten des initialen Prompts
    if 'persona_data' in st.session_state and 'company_data' in st.session_state and 'werbespot_data' in st.session_state:
        persona_data = st.session_state['persona_data']
        company_data = st.session_state['company_data']
        werbespot_data = st.session_state['werbespot_data']
        sonstiges_data = st.session_state['sonstiges_data']

    # Konvertieren der Daten in einen lesbaren String
        persona_str = ", ".join([f"{key}: {value}" for key, value in persona_data.items()])
        company_str = ", ".join([f"{key}: {value}" for key, value in company_data.items()])
        werbespot_str = ". ".join([f"{key}: {value}" for key, value in werbespot_data.items()])
        sonstiges_str = ", ".join([f"{key}: {value}" for key, value in sonstiges_data.items()])

        initial_prompt = (
        f"Hi! Wir sind das Unternehmen {company_data.get('unternehmensname', 'N/A')} und wir wollen einen Werbespot für unser neues Produkt {werbespot_data.get('produktname', 'N/A')} realisieren. Dafür brauchen wir aber ein Skript."
        f"Erstelle ein Werbespot-Skript anhand der folgenden Informationen.\n\n"
        
        f"**COMPASS**:\n"
        f"- **C - Context**: Die Werbung ist für das Unternehmen {company_data.get('unternehmensname', 'N/A')}, "
        f"das in der Branche {company_data.get('branche', 'N/A')} tätig ist. Die Zielgruppe hat Interessen wie {persona_data.get('interessen', 'N/A')}. "
        f"Der Werbespot soll das Ziel {werbespot_data.get('ziel_der_werbung', 'N/A')} erreichen.\n\n"
        f" <Mehr Details zum Unternehmen und zur Zielgruppe>\n\n"
        f"**Unternehmensinformationen**:\n{company_str}\n\n"
        f"**User Persona der Zielgruppe**:\n{persona_str}\n\n"
        f"**Werbespot-Details**:\n{werbespot_str}\n\n"
        f"**Sonstiges**:\n{sonstiges_str}\n\n"
        f"</Mehr Details zum Unternehmen und zur Zielgruppe>\n\n"

        f"- **O - Objective**: Das Ziel des Prompts ist das Generieren eines Skriptes für ein Werbespot für das Unternehmen und ihr Produkt. Ziel des Werbespots ist es, {werbespot_data.get('ziel_der_werbung', 'N/A')} zu erreichen, "
        f"indem die {werbespot_data.get('usps', 'N/A')} hervorgehoben werden und eine {werbespot_data.get('ton_und_stil', 'N/A')} Botschaft vermittelt wird.\n\n"

        f"- **M - Mode**: Du bist ein Skriptautor, der ein Werbespot-Skript für das Unternehmen {company_data.get('unternehmensname', 'N/A')} und ihr Produkt {werbespot_data.get('produktname', 'N/A')} erstellt."
        "Der Ton des Werbespots sollte {werbespot_data.get('ton_und_stil', 'N/A')} sein. "
        f"Die Sprache sollte ansprechend und überzeugend sein, um die Zielgruppe effektiv anzusprechen.\n\n"

        f"- **P - People of Interest**: Die Zielgruppe umfasst {persona_data.get('alter', 'N/A')}-jährige {persona_data.get('geschlecht', 'N/A')}, "
        f"die Interessen wie {persona_data.get('interessen', 'N/A')} und Werte wie {persona_data.get('werte', 'N/A')} haben. "
        f"Sie neigen dazu, {persona_data.get('einkaufsgewohnheiten', 'N/A')} und bevorzugen Marken wie {persona_data.get('markenpraferenzen', 'N/A')}.\n\n"
        
        f"- **A - Attitude**: Die Einstellung des Werbespots sollte {werbespot_data.get('ton_und_stil', 'N/A')} sein, "
        f"um ein positives und ansprechendes Bild der Marke zu vermitteln.\n\n"

        f"- **S - Style**: Der Stil sollte {werbespot_data.get('ton_und_stil', 'N/A')} und ansprechend für die Zielgruppe sein. "
        f"Die Hauptbotschaft sollte klar und überzeugend dargestellt werden.\n\n"

        f"- **Zusätzliche Hinweise**: "
        f"Stelle sicher, dass alle Elemente des Werbespots harmonisch zusammenarbeiten und die gewünschte Wirkung auf die Zielgruppe haben. "
        f"Denke daran, die einzigartigen Verkaufsargumente (USPs) hervorzuheben und eine klare Call-to-Action zu integrieren.\n\n"

        f"**Zusammenfassung aller gesammelten Daten**:\n"
        f"**User Persona der Zielgruppe**:\n{persona_str}\n\n"
        f"**Unternehmensinformationen**:\n{company_str}\n\n"
        f"**Werbespot-Details**:\n{werbespot_str}\n\n"
        f"**Sonstiges**:\n{sonstiges_str}\n\n"

        f"Bitte stelle sicher, dass das Skript die oben genannten Punkte berücksichtigt und an die bereitgestellten Daten angepasst wird.\n\n"
        f"Bitte arbeite schrittweise und nimm Verbesserungsvorschläge an. Hier sind einige Punkte, die dir helfen können, bessere Ergebnisse zu erzielen:\n\n"
        f"- **Schrittweise Vorgehensweise**: Zerlege komplexe Aufgaben in kleinere Schritte und arbeite diese nacheinander ab. Dies erleichtert es, den Überblick zu behalten und Fehler zu vermeiden.\n\n"
        f"- **Verbesserungsvorschläge**: Sei offen für Vorschläge und Korrekturen. Betrachte sie als Möglichkeit, das Ergebnis zu verbessern.\n\n"
        f"- **Positive Rückmeldungen**: Achte auf die Hinweise, die dir bestätigen, dass du auf dem richtigen Weg bist. Diese helfen dir zu erkennen, was gut funktioniert.\n\n"
        f"- **Hilfe nutzen**: Nutze alle verfügbaren Informationen und Hinweise, um die gestellten Aufgaben bestmöglich zu erfüllen."
    )


    else:
         initial_prompt = "Bitte geben Sie Informationen zur User Persona, zum Unternehmen und zum Werbespot ein."

# Anzeigen des initialen Prompts
    st.text_area("Initialer Prompt (kopieren und bei Bedarf bearbeiten):", initial_prompt, height=100)


# Chat input and message creation with file ID
    if prompt := st.chat_input("Wie kann ich Ihnen helfen?"):
        with st.chat_message('user'):
            st.write(prompt)

        message_data = {
            "thread_id": st.session_state.thread.id,
            "role": "user",
            "content": prompt
        }

    # Include file ID in the request if available
        if "file_id" in st.session_state:
            message_data["file_ids"] = [st.session_state.file_id]

        st.session_state.messages = client.beta.threads.messages.create(**message_data)

        st.session_state.run = client.beta.threads.runs.create(
            thread_id=st.session_state.thread.id,
         assistant_id=st.session_state.assistant.id,
        )
        if st.session_state.retry_error < 3:
            time.sleep(1)
            st.rerun()

# Handle run status
    if hasattr(st.session_state.run, 'status'):
        if st.session_state.run.status == "running":
            placeholder = st.empty()
            with placeholder.container():
                with st.chat_message('assistant'):
                    st.write("Thinking ......")

        elif st.session_state.run.status == "failed":
            st.session_state.retry_error += 1
            with st.chat_message('assistant'):
                if st.session_state.retry_error < 3:
                    st.write("Run failed, retrying ......")
                    time.sleep(3)
                    st.rerun()
                else:
                    st.error("FAILED: The OpenAI API is currently processing too many requests. Please try again later ......")

        elif st.session_state.run.status != "completed":
            st.session_state.run = client.beta.threads.runs.retrieve(
                thread_id=st.session_state.thread.id,
                run_id=st.session_state.run.id,
         )
            if st.session_state.retry_error < 3:
                time.sleep(3)
                st.rerun()


if __name__ == "__main__":
    app()


# # Anzeigen des initialen Prompts
#     st.text_area("Initialer Prompt (kopieren und bei Bedarf bearbeiten):", initial_prompt, height=100)
# 
#     if st.button("Skript generieren"):
#         with st.spinner("Das Skript wird generiert..."):
#             response = openai.Completion.create(
#                 engine="davinci-codex",
#                 prompt=initial_prompt,
#                 max_tokens=500
#             )
# 
#         st.success("Skript erfolgreich generiert!")
#         st








