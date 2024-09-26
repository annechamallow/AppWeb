import streamlit as st 
from openai import OpenAI

st.title("Anne-ChatGPT")

openai_key = st.sidebar.text_input("Collez ici votre clé OpenAI :", '')
client = OpenAI(api_key = openaikey)

prompt = st.text_input("Tapez votre prompt : ")

chat_completion = client.chat.completions.create(
      message=prompt,
      model="gpt-3.5-turbo",
      temperature=0.3,
      max_tokens=100,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0,
)

st.write(chat_completion.choices[0].message.content)
