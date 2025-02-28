import streamlit as st
import google.generativeai as genai
apikey="AIzaSyD9EEsyenFPc3O_wbe7Eohd9tA7Uc9vuDc"
genai.configure(api_key=apikey)
model=genai.GenerativeModel('gemini-1.5-flash')
if "chat not in st.session_state:
    st.session_state.chat=model.start_chat(history[])
st.title("Chatbot-Your AI Assistant")
st.write('This is an AI Chatbot to solve your queries.....')

if "messages" not in st.session_state:
  st.session_state.messages=[]

for messagein st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])
if prompt:= st.chat_input("Say something..."):
  st.session_state.messages.append({"role": "user", "content" : prompt})
  with st.chat_message("user"):
    st.markdown(prompt)
  response=st.session_state.chat.send_message(prompt)
  st.session_state.messages.append({"role":"assistant", "content" : response.text})
  with 
