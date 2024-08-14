import os

import streamlit as st
import pandas as pd

df = pd.read_csv(os.path.join(os.getcwd(),"arquivos","spotify.csv"))
#df.set_index("Artist", inplace=True)
best_df_stream = df[df["Stream"] > 1000000000]["Stream"]

st.set_page_config(
    layout="wide",
    page_title="Spotify Songs"
)
#Indice para filtro de artistas para gráfico Stream x música
df.set_index("Track", inplace=True)
#Tabela com dados sob condição acima
#st.write(best_df)

#Gráfico de linha comparando Stream com bandas/cantores
st.line_chart(best_df_stream)


#Criação de filtro selectbox para artistas no gráfico de barras
## Cria lista com index de cada artista (value_counts retorna index únicos)
artists = df["Artist"].value_counts().index
## Criação do filtro com o selectbox
artist = st.selectbox("Artista", artists)
df_filtered = df[df["Artist"] == artist]
df_filtered_stream = df[df["Artist"] == artist]["Stream"]

albuns = df_filtered["Album"].value_counts().index
album = st.selectbox("Album", albuns)
df_filtered_stream_2 = df[df["Album"] == album]["Stream"]

#Checkbox para exibição do gráfico de barras
display = st.checkbox('Display')

if display:
    # Gráfico de barras filtrado
    #st.bar_chart(df_filtered_stream)
    st.bar_chart(df_filtered_stream_2)




