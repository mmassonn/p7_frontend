import streamlit as st
import requests

# Titre de l'app.
st.title("Analyseur de Sentiment")

# Zone de text.
message = st.text_area("Entrez votre message ici")

# Bouton d'analyse.
def analyser_sentiment(message):
    url = 'https://ocp7webapp-etdkd3djg4eyhwhg.canadacentral-01.azurewebsites.net/predict'
    print(f"url is : {url}")
    data = {'text': message}
    response = requests.post(url, json=data)
    prediction = response.json()['prediction']
    return prediction

if st.button("Analyser le sentiment"):
    prediction = analyser_sentiment(message)
    st.write("Le sentiment est : ", prediction)

def feedback_user(message, prediction):
    url = 'https://ocp7webapp-etdkd3djg4eyhwhg.canadacentral-01.azurewebsites.net/log_trace'
    data = {"text": message, 
            "predicted_sentiment": prediction
            }
    requests.post(url, json=data)

prediction = None

if st.button("La prédiction n'est pas correct"):
    prediction = analyser_sentiment(message)
    feedback_user(message=message, prediction=prediction)
    st.write("Merci pour votre retour !")
