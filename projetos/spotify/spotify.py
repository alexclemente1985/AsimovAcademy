import os

import streamlit as st
import pandas as pd
import time

st.set_page_config(
    layout="wide",
    page_title="Spotify Songs"
)

@st.cache_data
def load_data():
    df = pd.read_csv(os.path.join(os.getcwd(), "arquivos", "spotify.csv"))
    #Simulando carregamentos demorados (5 segundos)
    ## Só vai ocorrer na primeira vez, pois nas demais a informação já estará no cache
    time.sleep(5)
    return df

df = load_data()
#Session State
if "df_spotify" not in st.session_state:
    st.session_state["df_spotify"] = df


#df.set_index("Artist", inplace=True)
best_df_stream = df[df["Stream"] > 1000000000]["Stream"]


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
#artist = st.selectbox("Artista", artists)
## Atualização para sidebar
artist = st.sidebar.selectbox("Artista", artists)
df_filtered = df[df["Artist"] == artist]
df_filtered_stream = df[df["Artist"] == artist]["Stream"]

albuns = df_filtered["Album"].value_counts().index
#album = st.selectbox("Album", albuns)
## Atualização para sidebar
album = st.sidebar.selectbox("Album", albuns)

df_filtered_stream_2 = df[df["Album"] == album]["Stream"]

#Checkbox para exibição do gráfico de barras
display = st.checkbox('Display')

if display:
    # Gráfico de barras filtrado
    #st.bar_chart(df_filtered_stream)
    st.bar_chart(df_filtered_stream_2)

# Colunas
df_filtered_album = df[df["Album"] == album]
col1, col2 = st.columns(2)

col1.bar_chart(df_filtered_stream_2)
col2.line_chart(df_filtered_album["Danceability"])

# Colunas com larguras diferentes
col3, col4 = st.columns([0.7,0.3])
col3.bar_chart(df_filtered_stream_2)
col4.line_chart(df_filtered_album["Danceability"])

st.sidebar.button("Teste")




