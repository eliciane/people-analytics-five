import streamlit as st
import pandas as pd
import streamlit_pandas as sp

st.title('Mapeamento das Competências')
st.title('Analytics Prep')

#importar dataset
df = st.dataframe(pd.read_csv('analy_prep.csv'))
st.subheader("Dados: Skills Analytics Prep")
st.write(df)
