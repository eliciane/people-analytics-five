    import pandas as pd
    import streamlit as st
    #import plotly.express as px
    #import matplotlib.pyplot as plt
    #import numpy as np
    #import warnings

    #pd.set_option('display.expand_frame_repr', False)
    #warnings.filterwarnings("ignore")

    # Set the app title
    st.title('Mapeamento das Competências')
    st.title('Analytics Prep')

    #importar dataset
    #file_path = "/home/eliciane/PycharmProjects/people-analytics-five/dados/Mapeamento_Competencias_08nov.csv"
    #df = pd.read_csv(file_path)


    #df = st.dataframe(pd.read_csv('dados/Mapeamento_Competencias_08nov.csv'))


    # Skills Analytics Prep
    #df_equipe = df[['ID', 'Squad']].copy() # colunas ID e equipe
    #df_analy = df[['Analy_ PREP _Alteryx', 'Analy_ PREP _SAS','Analy_ PREP _Pentaho Data Integration', 'Analy_ PREP _Power Center','Analy_ PREP _SAP Analytics Cloud','Analy_ PREP _Oracle Data Integration','Analy_ PREP _SQL Server Integration Services']].copy()

    #df_analy = df.iloc[:,19:26] # colunas BI
    #df_concat_analy = pd.concat([df_equipe, df_analy], axis = 1)



    #df_equipe = df_equipe.to_csv('/home/eliciane/PycharmProjects/people-analytics-five/dados/df_equipe.csv', index=False)
    #df_analy = df_analy.to_csv('/home/eliciane/PycharmProjects/people-analytics-five/dados/df_analy.csv', index=False)

    #df_equipe= pd.read_csv('/home/eliciane/PycharmProjects/people-analytics-five/dados/df_equipe.csv')
    #df_analy = pd.read_csv('/home/eliciane/PycharmProjects/people-analytics-five/dados/df_analy.csv')

    #df_equipe = st.dataframe(pd.read_csv('/dados/df_equipe.csv'))
    #df_analy = st.dataframe(pd.read_csv('/dados/df_analy.csv'))

    #df_concat_analy = pd.concat([df_equipe, df_analy], axis = 1)
    #print(df_concat_analy.head(4)) # imprime somente as quatro primeiras linhas
    #print(df_concat_analy.tail(4)) # imprime somente as quatro primeiras linhas
    #df_concat_analy = df_concat_analy.to_csv('/home/eliciane/PycharmProjects/people-analytics-five/dados/analy_prep.csv', index=False)

    df_concat_analy = st.dataframe(pd.read_csv('dados/analy_prep.csv'))

    st.subheader("Dados: Skills Analytics Prep")
    st.dataframe(df_concat_analy)