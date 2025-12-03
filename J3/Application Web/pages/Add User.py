import requests
import streamlit as st

with st.form('add_user'):

    name = st.text_input('Your name')
    age = st.text_input('Your age')
    city = st.text_input('Your city')

    if st.form_submit_button('Add User'):
        data ={
            'name':name,
            'age':age,
            'city':city}

        requests.post("http://127.0.0.1:8000/add_user", json=data).text