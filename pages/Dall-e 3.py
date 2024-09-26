import streamlit as st

st.title("Générateur d'images Dall-e 3")

st.text("Entrez votre prompt ici :")
prompt = st.input

from openai import OpenAI
client = OpenAI(api_key=OpenAIKEY)

image = client.images.generate(
    model="dall-e-2",
    prompt=prompt,
    size="512x512",
    quality="standard",
    n=1,
)

image_url = image.data[0].url
print(image_url)

st.image("image_url")
