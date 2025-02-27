import streamlit as st
import openai

# Load API key from secrets
openai.api_key = "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"

st.title("FinTech Chatbot")
st.write("Ask me anything about loans, credit scores, and interest rates!")

user_input = st.text_input("You:", "")


if user_input:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    st.write("Chatbot:", response["choices"][0]["message"]["content"])
