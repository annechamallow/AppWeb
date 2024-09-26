import streamlit as st

st.title("Générateur d'images Dall-e 3")

OpenAIKey = st.sidebar.text_input("Collez ici votre clé OpenAI :")

st.text_input("Entrez votre prompt ici :")


from openai import OpenAI
client = OpenAIKey

image = client.image.generate(
    model="dall-e-3",
    prompt = st.text_input,
    size="512x512",
    quality="standard",
    n=1,
)

image_url = image.data[0].url

st.image(image_url)
