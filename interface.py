import streamlit as st
import requests

# Titre de l'app.
st.title("Analyseur de Sentiment")

# Zone de text.
message = st.text_area("Entrez votre message ici")

# Bouton d'analyse.
def analyser_sentiment(message):
    url = 'https://badbuzzwebapp-f3brayd9dmgfcsb8.canadacentral-01.azurewebsites.net/'
    data = {'text': message}
    response = requests.post(url, json=data)
    print(response)
    prediction = response.json()['prediction']
    return prediction


if st.button("Analyser le sentiment"):
    prediction = analyser_sentiment(message)
    st.write("Le sentiment est : ", prediction)
