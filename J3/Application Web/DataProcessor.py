import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time

time_local = time.localtime()
date_now = time.strftime("%Y-%m-%d %H:%M:%S", time_local)

st.title('Application DataProcessor')

file = st.file_uploader('Versez votre fichier',type='csv')

if file:
    df = pd.read_csv(file)

    if st.checkbox('Affichage graphique'):
        cols = st.multiselect("Sélectionnez 2 colonnes max", 
                            df.columns, 
                            
                            max_selections=2)
        if len(cols) == 2:
            fig = plt.figure(figsize=(10, 5))
            sns.boxenplot(df, x=cols[0], y=cols[1])
            st.pyplot(fig)

    if st.checkbox('Edition du Dataframe'):
        df = st.data_editor(df)
        
        st.download_button('Télécharger le csv',
                           df.to_csv().encode("utf-8"),
                           file_name=date_now +' data.csv'
                           )





    
    

