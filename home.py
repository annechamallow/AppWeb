import streamlit as st

# Titre
st.title("Mon formulaire")

# Text
st.write("Voici un petit formulaire de contact à remplir :")

# Champ de saisie
user_input = st.text_input("Entrez votre texte :")
st.write(user_input)

# Image
st.image("https://tempo.cdn.tambourine.com/windsong/media/bmot-website-homepage-header-desktop-65f9c01c2da38.mp4")

# Sidebar
st.sidebar.title("Anne-Charlotte Raimbault")
st.sidebar.video("https://www.youtube.com/watch?v=AsVdSicpGpY")

# Select bar
student_grade = st.selectbox("Sélectionnez votre niveau d'études :", ["Bac","Bac +2", "Bac +3", "Bac +4", "Bac +5"])

# Select slider
age = st.select_slider("Indiquez votre âge", range(0,99))

# Conditions en python
if age >= 18:
  st.write("Vous êtes majeur")
else:
  st.write("Vous êtes mineur") 
