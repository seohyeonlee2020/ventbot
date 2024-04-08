import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat

st.set_page_config(page_title="ventbot - talk about anything")

if 'bot_response' not in st.session_state:
    st.session_state['bot_response'] = ["Hi, what do you want to talk about today?"]
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = ['Hello!']

input_container = st.container()
colored_header(label='', description='', color_name='blue-30')
response_container = st.container()

# User input
def get_input():
    input_text = st.text_input("You: ", "", key="input")
    return input_text

with input_container:
    user_input = get_input()

# Response output
def generate_response(prompt):
    chatbot = hugchat.ChatBot(cookie_path="cookies.json")
    response = chatbot.chat(prompt)
    return response

with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.user_input.append(user_input)
        st.session_state.bot_response.append(response)
        
    if st.session_state['bot_response']:
        for i in range(len(st.session_state['bot_response'])):
            user_input_message = st.session_state['user_input'][i]
            bot_response_message = st.session_state['bot_response'][i]
            
            # Ensure messages are JSON-compatible (e.g., use string representation)
            message(user_input_message, is_user=True, key=str(i)+ '_user')
            message(str(bot_response_message), key=str(i))  # Convert bot response to string


