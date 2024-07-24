# Willkommen.py
import streamlit as st

def app():
    st.title('Willkommen zu Ihrem Streamlit Werbespot Generator!')
    st.write(
        "Dieses Tool hilft Ihnen dabei, einen Werbespot für Ihr Unternehmen zu erstellen. "
        "Folgen Sie einfach den Schritten auf der linken Seite, um Ihren Werbespot zu generieren."
    )
    st.subheader('Anleitung')
    st.write(
        "1. **Unternehmensinformationen**: Geben Sie Informationen zu Ihrem Unternehmen ein, "
        "wie den Namen, die Branche und die Unternehmensgröße."
    )
    st.write(
        "2. **Werbespot**: Erstellen Sie ein Skript für Ihren Werbespot, indem Sie Details zu Ihrem Produkt, "
        "der Zielgruppe und dem gewünschten Stil angeben."
    )
    st.write(
        "3. **User Persona**: Definieren Sie die Merkmale Ihrer Zielgruppe, wie Alter, Geschlecht und Interessen."
    )
    st.write(
        "4. **Sonstiges**: Geben Sie zusätzliche Informationen an, die für die Erstellung des Werbespots relevant sind."
    )
    st.write(
        "5. Speichern Sie Ihre Daten auf jeder Seite, bevor Sie zur nächsten Seite wechseln."
    )
    st.write(
        "6. Nachdem Sie alle Informationen eingegeben haben, können Sie auf die Seite 'OpenAI' gehen, um ein Skript für Ihren Werbespot zu generieren."
    )
    st.write(
        "7. Den Prompts folgen und die generierten Skripte anpassen, um sie an Ihre Bedürfnisse anzupassen."
    )
    st.write(
        "8. Viel Spaß beim Erstellen Ihres Werbespots!"
    )

    st.subheader('Hinweise')
    st.write(
        "1. **Sicherheitshinweis**: Bitte geben Sie keine sensiblen Daten ein, da diese in Ihrem Browser gespeichert werden."
    )
    st.write(
        "2. **Speichern Sie Ihre Daten**: Stellen Sie sicher, dass Sie Ihre Daten auf jeder Seite speichern, "
        "bevor Sie zur nächsten Seite wechseln."
    )
    st.write(
        "3. **Download-Optionen**: Auf der Seite 'Daten' können Sie Ihre gespeicherten Daten als Textdatei herunterladen."
    )
    st.write(
        "4. **Chat mit OpenAI**: Auf der Seite 'OpenAI' können Sie einen Chat mit einem OpenAI-Modell starten, "
        "um Ideen für Ihren Werbespot zu erhalten."
    )
    st.write(
        "5. **Feedback und Verbesserungsvorschläge**: Wir freuen uns über Ihr Feedback und Ihre Verbesserungsvorschläge. "
        "Bitte zögern Sie nicht, uns Ihre Gedanken mitzuteilen."
        "Sie können uns auch eine E-Mail an [test1234@gmail.com] senden."
    )
    st.write(
        "6. **Viel Spaß!**: Genießen Sie die Erstellung Ihres Werbespots und lassen Sie Ihrer Kreativität freien Lauf."
    )

# Dieser Teil ist für Testzwecke, wenn Sie dieses Skript einzeln laufen lassen.
if __name__ == "__main__":
    app()
