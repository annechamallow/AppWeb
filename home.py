import streamlit as st

# Titre
st.title("Mon formulaire")

# Text
st.write("Voici un petit formulaire de contact à remplir :")

# Champ de saisie
user-input = st.text_input("Entrez votre texte :")

st.write(user-input)
