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
    prediction = response.json()['prediction']
    return prediction

def feedback_user(message, prediction):
    url = 'oc7badbuzz-cxetazfvbharfdfc.canadacentral-01.azurewebsites.net/log_trace'
    data = {"text": message, 
            "predicted_sentiment": prediction
            }
    requests.post(url, json=data)

prediction = None

if st.button("Analyser le sentiment"):
    prediction = analyser_sentiment(message)
    st.write("Le sentiment est : ", prediction)

if st.button("La prédiction n'est pas correct"):
    if prediction is not None:
        print(f"le message {message} a un sentiment {prediction}")
        feedback_user(message=message, prediction=prediction)
        st.write("Merci pour votre retour !")
    else:
        st.write("Veuillez d'abord analyser le sentiment.")
