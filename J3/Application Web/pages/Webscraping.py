import streamlit as st
from dawan.gestion import get_article

st.title("WebScraping")

with st.form("scraping"):

    search_subject = st.text_input("Sujet recherché")
    if st.form_submit_button("Lancer le scraping"):
        get_article(search_subject)
