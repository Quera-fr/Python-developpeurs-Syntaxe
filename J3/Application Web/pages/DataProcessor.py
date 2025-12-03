import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import seaborn as sns

st.set_page_config(
    page_title='Application DataProcess',
    layout='wide',
    page_icon='https://www.dawan.fr/assets/images/logo-dawan-9d53226aeca7ee3e80897245589719e7.svg'
)

df = pd.read_csv("https://raw.githubusercontent.com/Quera-fr/Python-Programming/refs/heads/main/data.csv")

st.title("Edition d'un DataFrame")

df = st.data_editor(df, width=4000)

gender = st.selectbox("Selectionnez un Genre", df.Gender.unique())

# Création d'un graphique
if st.button('Afficher le graphique'):
    fig = plt.figure(figsize=(10, 5))
    sns.histplot(df[df["Gender"] == gender].Age)
    st.pyplot(fig)