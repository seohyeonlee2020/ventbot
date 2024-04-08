import streamlit as st

st.title("vent-bot")
st.write("Vent anything here")
name = st.text_input(label="name input",placeholder="Enter your name", max_chars=50)
if st.button('Submit'):
    st.write('Hi ' + name + ". What do you want to talk about today?")
