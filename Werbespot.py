# werbespot.py
import streamlit as st

def app():
    st.title('Informationen zur Erstellung des Werbespot-Skripts')
    st.write(
        "Für das Erstellen des Skriptes, brauchen wir die folgenden Informationen. "
        "Bitte versuchen Sie so detailiert wie möglich zu sein, um ein passendes Skript zu erstellen. "
        "Füllen Sie das Formular aus und klicken Sie auf 'Skriptdaten speichern', um die Daten zu speichern."
    )

    # Eingabefelder für die Erstellung eines Werbespot-Skripts
    with st.form(key='werbespot_form'):
        unternehmensname = st.text_input("Name des Unternehmens")
        produktname = st.text_input("Name des Produkts")
        produkt_details = st.text_area("Produktdetails (z.B. Funktionen, Vorteile, Anwendungsbereiche)")
        branche = st.text_input("Branche")

        # Optionen für das Ziel der Werbung
        optionen = [
            "Markenbewusstsein",
            "Produktverkauf",
            "Kundenbindung",
            "Markteinführung",
            "Imagepflege",
            "Lead-Generierung",
            "Kundengewinnung",
            "Produktinformation",
            "Event-Promotion",
            "Marktforschung"
        ]

        # Dropdown-Funktion mit Mehrfachauswahl
        ziel_der_werbung = st.multiselect(
            "Ziel der Werbung (z.B. Markenbewusstsein, Produktverkauf, Kundenbindung)",
            options=optionen,
            default=None
        )  

        usps = st.text_area("Unique Selling Propositions (USPs) des Produkts")

        veröffentlichungskanal = st.selectbox("Veröffentlichungskanal", ["TV", "Radio", "Online", "Social Media", "Kino"])
        social_media_format = st.selectbox("Social Media Format (optional)", ["Kurzes Reel", "Shortmovie", "Story", "Post"])

        # Optionen für den Ton und Stil des Werbespots
        ton_und_stil_optionen = [
            "Humorvoll",
            "Seriös",
            "Emotional",
            "Inspirierend",
            "Informativ",
            "Dramatisch",
            "Unterhaltsam",
            "Romantisch",
            "Abenteuerlich",
            "Mysteriös"
        ]

        # Dropdown-Funktion für den Ton und Stil des Werbespots
        ton_und_stil = st.multiselect(
            "Ton und Stil des Werbespots (z.B. humorvoll, seriös, emotional)",
            options=ton_und_stil_optionen,
            default=None
        )

        laenge = st.slider("Länge des Werbespots (in Sekunden)", 5, 120, 30)
        handlung_hauptbotschaft = st.text_area("Handlung oder Hauptbotschaft des Werbespots")
        call_to_action = st.text_area("Call to Action (z.B. 'Jetzt kaufen', 'Mehr erfahren', 'Anrufen')")
        sprache_des_werbespots = st.text_input("Sprache des Werbespots")
        zusatzliche_anmerkungen = st.text_area("Zusätzliche Anmerkungen oder Wünsche")

        # Knopf zum Absenden des Formulars
        submit_button = st.form_submit_button("Skriptdaten speichern")

        if submit_button:
            # Speichern der Werbespot-Daten im session_state
            st.session_state['werbespot_data'] = {
                "unternehmensname": unternehmensname,
                "produktname": produktname,
                "produkt_details": produkt_details,
                "branche": branche,
                "ziel_der_werbung": ziel_der_werbung,
                "usps": usps,
                "veröffentlichungskanal": veröffentlichungskanal,
                "social_media_format": social_media_format,
                "ton_und_stil": ton_und_stil,
                "laenge": laenge,
                "handlung_hauptbotschaft": handlung_hauptbotschaft,
                "call_to_action": call_to_action,
                "sprache_des_werbespots": sprache_des_werbespots,
                "zusatzliche_anmerkungen": zusatzliche_anmerkungen
            }

            st.success("Werbespot-Daten erfolgreich gespeichert!")

# Dieser Teil ist für Testzwecke, wenn Sie dieses Skript einzeln laufen lassen.
if __name__ == "__main__":
    app()
