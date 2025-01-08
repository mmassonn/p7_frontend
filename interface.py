import streamlit as st
import requests

# Titre de l'app.
st.title("Analyseur de Sentiment")

# Zone de text.
message = st.text_area("Entrez votre message ici")

# Bouton d'analyse.
def analyser_sentiment(message):
    url = 'https://oc7badbuzz-cxetazfvbharfdfc.canadacentral-01.azurewebsites.net/predict'
    data = {'text': message}
    response = requests.post(url, json=data)
    print(response)
    prediction = response.json()['prediction']
    return prediction


if st.button("Analyser le sentiment"):
    prediction = analyser_sentiment(message)
    st.write("Le sentiment est : ", prediction)

def feedback_user(message):
    url = 'oc7badbuzz-cxetazfvbharfdfc.canadacentral-01.azurewebsites.net/log_trace'
    data = {"text": message, 
            "predicted_sentiment": prediction
            }
    requests.post(url, json=data)

if st.button("La prédiction n'est pas correct"):
    feedback_user(message)
    st.write("Merci pour votre retour !")
