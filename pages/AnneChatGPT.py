import streamlit as st 
from openai import OpenAI

st.title("Anne-ChatGPT")

prompt = st.text_input("Tapez votre prompt : ")

openai_key = st.sidebar.text_input("Collez ici votre clé OpenAI :", '')
client = OpenAI(api_key = openai_key)

chat_completions = client.chat.completions.create(
            messages= [{
                        "role": "system",
                        "content": f"Tu réponds aux questions des utilisateurs",
                        },
                        { 
                        "role": "assistant",
                        "content": "Remplis le prompt",
                        },
                        {
                        "role": "user",
                        "content": prompt ,
                        }],
            model="gpt-3.5-turbo",
            temperature=0.3,
            max_tokens=100,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            )

st.write(chat_completion.choices[0].message.content)
