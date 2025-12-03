import streamlit as st

st.set_page_config(
    page_title='Application DataProcess',
    layout='wide',
    page_icon='https://www.dawan.fr/assets/images/logo-dawan-9d53226aeca7ee3e80897245589719e7.svg'
)

# Titre 
st.title("Application de traitement de données")

# Sous-titre
st.subheader('Première partie')

# Texte
st.write("2 décembre 2025")

# Checkbox
if st.checkbox("Afficher le champ de saisie"):
    # Champ de saisie
    user_input = st.text_input('Quel est votre nom ?')
    st.write(user_input)

# Création de colonne
col1, col2 = st.columns(2)

with col1:
    # Image
    st.image("https://www.dawan.fr/assets/images/logo-dawan-9d53226aeca7ee3e80897245589719e7.svg",
             width=2000)

with col2:
    # Video
    st.video("https://www.youtube.com/watch?v=Z-Nwo-ypKtM")

# Sidebar
st.sidebar.write('Bienvenue sur cette application')

