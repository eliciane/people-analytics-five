import streamlit as st
import pandas as pd

# importar dataset
#file_path = "/home/eliciane/PycharmProjects/people-analytics-five/dados/analy_prep.csv"
#df = pd.read_csv(file_path)
#print(df)

st.title('Mapeamento das Competências')
st.title('Analytics Prep')

#importar dataset#
df = st.dataframe(pd.read_csv('analy_prep.csv'))
st.subheader("Dados: Skills Analytics Prep")
st.write(df)
