import streamlit as st
import pandas as pd
import plotly.express as px

#Múltiplas páginas streamlit: criar pasta "pages" e inserir o arquivo da página

def top_100():
    st.set_page_config(layout="wide")
    st.write("Olá mundo com Streamlit!!!")

    df_reviews = pd.read_csv("../datasets/customer reviews.csv")
    df_top100_books = pd.read_csv("../datasets/Top-100 Trending Books.csv")

    st.write(df_reviews)
    st.write(df_top100_books)

    #Exibição de uma única coluna do dataframe
    st.write(df_reviews["book name"])

    #Corte do dataframe de acordo com uma condição (dentro do colchetes)
    st.write(df_top100_books[df_top100_books["book price"] < 50])

    #procura maior valor dentro da coluna de corte
    price_max = df_top100_books["book price"].max()

    #procura menor valor dentro da coluna de corte
    price_min = df_top100_books["book price"].min()

    #Slider na sidebar e criação de tabela filtrada em tempo real
    max_price = st.sidebar.slider("Price Range", price_min, price_max, price_max)
    df_books = df_top100_books[df_top100_books["book price"] <= max_price]
    st.write(df_books)

    #Gráfico de barras com plotly
    fig = px.bar(df_books["year of publication"].value_counts())
    # Gráfico de histograma
    fig2 = px.histogram(df_books["book price"])

    st.plotly_chart(fig)
    st.plotly_chart(fig2)

    #Colocando os gráficos anteriores um ao lado do outro
    col1, col2 = st.columns(2)
    col1.plotly_chart(fig)
    col2.plotly_chart(fig2)







if __name__ == '__main__':
    top_100()