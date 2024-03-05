import streamlit as st
import pandas as pd

# Trabalhando na página Book Reviews

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("../datasets/customer reviews.csv")
df_top100_books = pd.read_csv("../datasets/Top-100 Trending Books.csv")

# Retorna uma lista como sendo uma lista de strings individuais (com base no título dos livros)
books = df_top100_books["book title"].unique()

book = st.sidebar.selectbox("Books", books)

df_book = df_top100_books[df_top100_books["book title"] == book]
df_reviews_f = df_reviews[df_reviews["book name"] == book]

# st.write(df_book)
# st.write(df_reviews_f)

# Recurso do pandas para pegar um dos elementos da lista de retorno
book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = f"${df_book['book price'].iloc[0]}"
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

# Criando título e subtítulo
st.title(book_title)
st.subheader(book_genre)

# criando colunas de uma só vez, criando um painel
col1, col2, col3 = st.columns(3)
col1.metric("Price", book_price)
col2.metric("Rating", book_rating)
col3.metric("Year of publication", book_year)

# Linha divisória
st.divider()

# Reviews

for row in df_reviews_f.values:
    # printando as mensagens de feedback de usuários
    message = st.chat_message(f"{row[4]}")
    message.write(f"**{row[2]}**")
    message.write(row[5])
