import  os
import json
from idlelib.rpc import response_queue

import streamlit as st
import openai

#Configuring openai Api key
working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))
OPENAI_API_KEY = config_data["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY

# Configuring streamlit page settings
st.set_page_config(
    page_title = "GPT-4o-mini ChatBot",
    page_icon = "🐦‍🔥",
    layout = "centered"
)

#initialize chat session in streamlit if not already present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Streamlit page title
st.title("   🛕 GPT ChatBot   ")

#display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#input field for users message
user_prompt = st.chat_input("Ask GPT...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content":user_prompt})

    #send users message to gpt-4o and get response
    response = openai.chat.completions.create(
        model = "gpt-4o-mini",
        messages=[
            {"role":"system", "content":"You are a helpful assistant"},
            *st.session_state.chat_history
        ]
    )

    assistant_response = response.choices[0].message.content
    st.session_state.chat_history.append({"role":"assistant","content":assistant_response})

    #display gpt-4o-mini response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)