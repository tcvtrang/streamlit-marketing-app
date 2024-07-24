# page_four.py

import streamlit as st

def app():
    st.title('Data')

    # Check if persona_data is available in session state
    if 'persona_data' in st.session_state:
        persona_data = st.session_state['persona_data']

        # Format persona data as a plain text string
        persona_data_txt = "\n".join([f"{key}: {value}" for key, value in persona_data.items()])

        # Display persona data using markdown for better readability
        st.text("Persona")
        st.markdown(f"```\n{persona_data_txt}\n```")

        # Create a button to download the persona data as a .txt file
        st.download_button(
            label="Download Persona Data",
            data=persona_data_txt,
            file_name='persona_data.txt',
            mime='text/plain',
        )
    else:
        st.warning("Keine Persona-Daten gefunden. Bitte erstellen Sie eine User Persona auf der Seite 'Persona' zuerst.")

    
    # Check if werbespot_data is available in session state
    if 'werbespot_data' in st.session_state:
        werbespot_data = st.session_state['werbespot_data']

        # Format werbespot data as a plain text string
        werbespot_data_txt = "\n".join([f"{key}: {value}" for key, value in werbespot_data.items()])

        # Display werbespot data using markdown for better readability
        st.text("Werbespot")
        st.markdown(f"```\n{werbespot_data_txt}\n```")

        # Create a button to download the werbespot data as a .txt file
        st.download_button(
            label="Download Werbespot Data",
            data=werbespot_data_txt,
            file_name='werbespot_data.txt',
            mime='text/plain',
        )
    else:
        st.warning("Keine Werbespot-Daten gefunden. Bitte erstellen Sie einen Werbespot auf der Seite 'Werbespot' zuerst.")

    # Check if company_data is available in session state
    if 'company_data' in st.session_state:
        company_data = st.session_state['company_data']

        # Format werbespot data as a plain text string
        company_data_txt = "\n".join([f"{key}: {value}" for key, value in company_data.items()])

        # Display werbespot data using markdown for better readability
        st.text("Unternehmensinformationen")
        st.markdown(f"```\n{company_data_txt}\n```")

        # Create a button to download the werbespot data as a .txt file
        st.download_button(
            label="Download Unternehmensinformationen Data",
            data=company_data_txt,
            file_name='company_data.txt',
            mime='text/plain',
        )
    else:
        st.warning("Keine Unternehmensinformationen-Daten gefunden. Bitte erstellen Sie Unternehmensinformationen auf der Seite 'Unternehmensinformationen' zuerst.")

    # Check if sonstiges_data is available in session state
    if 'sonstiges_data' in st.session_state:
        sonstiges_data = st.session_state['sonstiges_data']

        # Format sonstiges data as a plain text string
        sonstiges_data_txt = "\n".join([f"{key}: {value}" for key, value in sonstiges_data.items()])

        # Display sonstiges data using markdown for better readability
        st.text("Sonstiges")
        st.markdown(f"```\n{sonstiges_data_txt}\n```")

        # Create a button to download the sonstiges data as a .txt file
        st.download_button(
            label="Download Sonstiges Data",
            data=sonstiges_data_txt,
            file_name='sonstiges_data.txt',
            mime='text/plain',
        )
    else:
        st.warning("Keine Sonstiges-Daten gefunden. Bitte erstellen Sie Sonstiges auf der Seite 'Sonstiges' zuerst.")