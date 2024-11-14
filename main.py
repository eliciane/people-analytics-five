import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
#import warnings

pd.set_option('display.expand_frame_repr', False)
#warnings.filterwarnings("ignore")

# Set the app title
st.title('Mapeamento das Competências')
st.title('Analytics Prep')

#importar dataset
#file_path = "/home/eliciane/PycharmProjects/people-analytics-five/dados/Mapeamento_Competencias_08nov.csv"

#file_path = "\dados\Mapeamento_Competencias_08nov.csv"

df = st.dataframe(pd.read_csv('dados/Mapeamento_Competencias_08nov.csv'))
#df = pd.read_csv(file_path)

# Skills Analytics Prep
df_equipe = df[['ID', 'Squad']].copy() # colunas ID e equipe
df_analy = df[['Analy_ PREP _Alteryx', 'Analy_ PREP _SAS',
       'Analy_ PREP _Pentaho Data Integration', 'Analy_ PREP _Power Center',
       'Analy_ PREP _SAP Analytics Cloud',
       'Analy_ PREP _Oracle Data Integration',
       'Analy_ PREP _SQL Server Integration Services']].copy()
#df_analy = df.iloc[:,19:26] # colunas BI
df_concat_analy = pd.concat([df_equipe, df_analy], axis = 1)
print(df_concat_analy.head(4)) # imprime somente as quatro primeiras linhas

st.subheader("Dados: Skills Analytics Prep")
st.dataframe(df_concat_analy)

#renomear colunas
df_concat_analy = df_concat_analy.rename(columns={'Analy_ PREP _Alteryx': 'AP_Alteryx',
                                        'Analy_ PREP _SAS': 'AP_SAS',
                                        'Analy_ PREP _Pentaho Data Integration': 'AP_PentahoDataInteg',
                                        'Analy_ PREP _Power Center': 'AP_PowerCenter',
                                        'Analy_ PREP _SAP Analytics Cloud': 'AP_SAPAnalyticsCloud',
                                        'Analy_ PREP _Oracle Data Integration':'AP_OracleDataInteg',
                                        'Analy_ PREP _SQL Server Integration Services': 'AP_SQLServerIntegServ'})

#criar uma lista de colunas
metrics_analy = df_concat_analy.columns[1:].tolist()

#verificar a média do time
df_analy_mean_serie = df_concat_analy[['AP_Alteryx','AP_SAS','AP_PentahoDataInteg','AP_PowerCenter','AP_SAPAnalyticsCloud', 'AP_OracleDataInteg', 'AP_SQLServerIntegServ']].mean().round(2)
df_analy_mean = df_analy_mean_serie.reset_index()
df_analy_mean = df_analy_mean.rename(columns={'index':'skills', 0:'média'} )
df_analy_mean = df_analy_mean.sort_values(by= 'média')

#imprimir no streamlit
st.subheader("Média Geral: Skills Analytics Prep")
st.dataframe(df_analy_mean)

fig = px.bar(df_analy_mean, x='skills', y='média', title='Gráfico da Média Geral: Skills Analytics Prep',
             labels={'skills': 'skills', 'média': 'média'},
             color_discrete_sequence=['#40798D'], text='média'
             )

# Melhorar a aparência do gráfico
fig.update_layout(
    xaxis_title="skills",
    yaxis_title="média",
    xaxis_tickangle=45,
    yaxis=dict(range=[0, 5])
)

st.plotly_chart(fig)
st.markdown("---")

#A seguir vamos calcular a média das competências de Analytics por squad"""

#df_concat_analy.columns
df_concat_analy_metrics = df_concat_analy[['Squad', 'AP_Alteryx', 'AP_SAS', 'AP_PentahoDataInteg',
       'AP_PowerCenter', 'AP_SAPAnalyticsCloud', 'AP_OracleDataInteg',
       'AP_SQLServerIntegServ']].copy()

#Abaixo temos a tabela e o gráfico de radar com média das competência de Análytics por Squad
#Incluindo título
df_analy_squads_mean = df_concat_analy_metrics.groupby('Squad').mean().round(2)
st.subheader("Média por Squads: Skills Analytics Prep")
st.dataframe(df_analy_squads_mean)

#reset index
df_analy_squads_mean = df_analy_squads_mean.reset_index()
# Reshape o formato para o grafico de radar
df_long = df_analy_squads_mean.melt(id_vars='Squad', var_name='Skills', value_name='Media')

# contruindo o gráfico
radar_chart_analyt = px.line_polar(df_long, r='Media',
                    theta='Skills',
                    color='Squad',
                    line_close=True,
                    color_discrete_sequence=['#00eb93', '#4ed2ff', '#9CDADB', '#FF00DE'],
                    template='plotly_dark')

radar_chart_analyt.update_polars(angularaxis_showgrid=False,
                  radialaxis_gridwidth=0,
                  gridshape='linear',
                  bgcolor='#494b5a',
                  radialaxis=dict(
                      tickvals=[1, 2, 3, 4, 5],  # Set custom tick values
                      range = [0, 5],
                      showticklabels=True  # Ensure tick labels are displayed
                      )
                  )

# Update layout to set legend font color and background
radar_chart_analyt.update_layout(
    paper_bgcolor='#2c2f36',
    legend=dict(
        font=dict(color='white'),  # Set legend font color
        bgcolor='#333333'          # Set legend background color
    )
)
st.subheader("Gráfico da Média por Squad: Skills Analytics Prep")
st.plotly_chart(radar_chart_analyt)
