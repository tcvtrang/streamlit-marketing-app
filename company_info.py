# company_info.py
import streamlit as st

def app():
    st.title('Unternehmensinformationen')
    st.write("Hier können Sie Informationen über Ihr Unternehmen eingeben. Diese Informationen werden verwendet, um den Werbespot an Ihr Unternehmen anzupassen.")

    # Eingabefelder für Unternehmensdaten
    with st.form(key='company_info_form'):
        unternehmensname = st.text_input("Unternehmensname")
        branche = st.text_input("Branche")
        groesse = st.selectbox("Unternehmensgröße", ["Kleinunternehmen", "Mittelständisch", "Großunternehmen"])

        # Informationen zu USPs und Zielen
        usps = st.text_area("USPs (Unique Selling Points)")
        ziele = st.text_area("Zielsetzungen der Kampagne")

        # Informationen zur Markenpersönlichkeit
        # Definieren Sie die Optionen für die Markenpersönlichkeit und -werte
        optionen = [
            "Innovativ",
            "Verlässlich",
            "Kundenorientiert",
            "Nachhaltig",
            "Kreativ",
            "Traditionell",
            "Modern",
            "Qualitätsbewusst",
            "Preiswert",
            "Luxuriös",
            "Authentisch"
        ]

        # Erstellen Sie eine Dropdown-Funktion mit Mehrfachauswahl
        markenpersoenlichkeit = st.multiselect(
            "Markenpersönlichkeit und -werte",
            options=optionen,
            default=None
        )

        # Informationen zu Hauptzielgruppen
        hauptzielgruppen = st.text_area("Hauptzielgruppen des Unternehmens")

        # Knopf zum Absenden des Formulars
        submit_button = st.form_submit_button("Unternehmensdaten speichern")

        if submit_button:
            # Speichern der Unternehmensdaten im session_state
            st.session_state['company_data'] = {
                "unternehmensname": unternehmensname,
                "branche": branche,
                "groesse": groesse,
                "usps": usps,
                "ziele": ziele,
                "markenpersoenlichkeit": markenpersoenlichkeit,
                "hauptzielgruppen": hauptzielgruppen
            }

            st.success("Unternehmensdaten erfolgreich gespeichert!")

# Dieser Teil ist für Testzwecke, wenn Sie dieses Skript einzeln laufen lassen.
if __name__ == "__main__":
    app()
