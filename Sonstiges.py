# user_persona.py
import streamlit as st

def app():
    st.title('Sonstiges')
    st.write("Hier können Sie weitere Informationen eingeben, die für die Erstellung des Werbespots relevant sind.")

    # Eingabefelder für grundlegende Informationen der User Persona
    with st.form(key='sonstiges_form'):
        budget = st.text_input("Budget für den Werbespot in Euro")
        darsteller_anzahl = st.slider("Wie viele Darsteller*innen wollen Sie einsetzen?", 0, 100, 5)  # Min, Max, Default
        skript_versionen = st.selectbox("Wie viele Skriptversionen brauchen Sie?", ["Eine", "Zwei", "Keine Angabe"])
        skript_art = st.selectbox("Welche Art von Skript benötigen Sie?", ["grob", "detailliert", "detailliert mit einer kurzen Zusammenfassung am Anfang"])
        zusatzliche_anmerkungen = st.text_area("Zusätzliche Anmerkungen oder Wünsche")

        # Knopf zum Absenden des Formulars
        submit_button = st.form_submit_button("Sonstige Daten speichern")

        if submit_button:
            # Speichern der Persona-Daten im session_state
            st.session_state['sonstiges_data'] = {
                "budget": budget,
                "skript_versionen": skript_versionen,
                "darsteller_anzahl": darsteller_anzahl,
                "skript_art": skript_art,
                "zusatzliche_anmerkungen": zusatzliche_anmerkungen
            }

            st.success("Sonstige Daten erfolgreich gespeichert!")

# Dieser Teil ist für Testzwecke, wenn Sie dieses Skript einzeln laufen lassen.
if __name__ == "__main__":
    app()
