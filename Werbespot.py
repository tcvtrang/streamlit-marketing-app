# werbespot.py
import streamlit as st

def app():
    st.title('Werbespot Skript Generator')

    # Eingabefelder für die Erstellung eines Werbespot-Skripts
    with st.form(key='werbespot_form'):
        unternehmensname = st.text_input("Name des Unternehmens")
        produktname = st.text_input("Name des Produkts")
        branche = st.text_input("Branche")
        zielgruppe = st.text_area("Zielgruppe des Werbespots (z.B. Alter, Geschlecht, Interessen)")
        ziel_der_werbung = st.text_area("Ziel der Werbung (z.B. Markenbewusstsein, Produktverkauf, Kundenbindung)")
        usps = st.text_area("Unique Selling Propositions (USPs) des Produkts")
        veröffentlichungskanal = st.selectbox("Veröffentlichungskanal", ["TV", "Radio", "Online", "Social Media", "Kino"])
        markenpersönlichkeit = st.text_area("Markenpersönlichkeit und -werte")
        ton_und_stil = st.text_area("Ton und Stil des Werbespots (z.B. humorvoll, seriös, emotional)")
        laenge = st.slider("Länge des Werbespots (in Sekunden)", 5, 120, 30)
        handlung_hauptbotschaft = st.text_area("Handlung oder Hauptbotschaft des Werbespots")
        call_to_action = st.text_area("Call to Action (z.B. 'Jetzt kaufen', 'Mehr erfahren', 'Anrufen')")
        zusatzliche_anmerkungen = st.text_area("Zusätzliche Anmerkungen oder Wünsche")

        # Knopf zum Absenden des Formulars
        submit_button = st.form_submit_button("Skriptdaten speichern")

        if submit_button:
            # Speichern der Werbespot-Daten im session_state
            st.session_state['werbespot_data'] = {
                "unternehmensname": unternehmensname,
                "produktname": produktname,
                "branche": branche,
                "zielgruppe": zielgruppe,
                "ziel_der_werbung": ziel_der_werbung,
                "usps": usps,
                "veröffentlichungskanal": veröffentlichungskanal,
                "markenpersönlichkeit": markenpersönlichkeit,
                "ton_und_stil": ton_und_stil,
                "laenge": laenge,
                "handlung_hauptbotschaft": handlung_hauptbotschaft,
                "call_to_action": call_to_action,
                "zusatzliche_anmerkungen": zusatzliche_anmerkungen
            }

            st.success("Werbespot-Daten erfolgreich gespeichert!")

# Dieser Teil ist für Testzwecke, wenn Sie dieses Skript einzeln laufen lassen.
if __name__ == "__main__":
    app()
