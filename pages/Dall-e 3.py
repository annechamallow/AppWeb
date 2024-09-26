import streamlit as st
from openai import OpenAI

st.title("Générateur d'images Dall-e 3")

OpenAIKey = st.sidebar.text_input("Collez ici votre clé OpenAI :")


prompt_image= st.text_input("Entrez votre prompt ici :")

client = OpenAI(OpenAIKey)

image = client.images.generate(
    model="dall-e-3",
    prompt = prompt_image,
    size="512x512",
    quality="standard",
    n=1,
)

image_url = image.data[0].url

st.image(image_url)
