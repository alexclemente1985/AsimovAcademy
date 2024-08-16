import os
import webbrowser
from datetime import datetime

import pandas as pd
import streamlit as st

# Carregamento dos dados
if "data" not in st.session_state:
    #df_data = pd.read_csv(os.path.join(os.getcwd(), "datasets", "CLEAN_FIFA23_official_data.csv"), index_col=0)
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)

    # Filtro para carregar jogadores que ainda estejam no contrato do clube
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    # Exclusão de jogadores sem valores registrados
    df_data = df_data[df_data["Value(£)"] >0]
    df_data = df_data.sort_values(by="Overall", ascending=False)

    st.session_state["data"] = df_data

st.markdown("# FIFA23 OFFICIAL DATASET!")
st.sidebar.markdown("Desenvolvido por [Alexandre C. Pinheiro] em aulas da Asimov Academy")

btn = st.link_button("Acesse os dados no Kaggle", "https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")
#if btn:
#    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

st.markdown(
    """
    O conjunto de dados contém uma vasta gama de atributos, incluindo dados demográficos dos jogadores, 
    caraterísticas físicas, estatísticas de jogo, detalhes do contrato e afiliações a clubes.
    
    Com **mais de 17 000 registros**, este conjunto de dados oferece um recurso valioso para analistas de futebol, 
    investigadores e entusiastas interessados em explorar vários aspectos do mundo do futebol, uma vez que permite 
    estudar os atributos dos jogadores, as métricas de desempenho, a avaliação do mercado, a análise dos clubes, 
    o posicionamento dos jogadores e o desenvolvimento dos jogadores ao longo do tempo.
    """
)
