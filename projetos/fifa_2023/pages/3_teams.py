import streamlit as st

st.set_page_config(
    page_title="Teams",
    layout="wide"
)

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

# Cria um filtro baseado na escolha do time na selectbox, e cria indices baseados nos nomes do jogadores
df_filtered = df_data[(df_data["Club"] == club)].set_index("Name")

st.image(df_filtered.iloc[0]["Club Logo"])
st.markdown(f"## {club}")

columns = ["Age", "Photo", "Flag", "Overall", "Value(£)", "Wage(£)", "Joined", "Height(cm.)", "Weight(lbs.)",
           "Contract Valid Until", "Release Clause(£)"]

# Permite configurações especiais na tabela do dataframe
st.dataframe(df_filtered[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     "Overall", format="%d", min_value=0, max_value=100
                 ),
                 "Wage(£)": st.column_config.ProgressColumn(
                     "Weekly Wage", format="£%d", min_value=0, max_value=df_filtered["Wage(£)"].max() #ponderação pelo maior salário do clube
                 ),
                 "Photo": st.column_config.ImageColumn(),
                 "Flag": st.column_config.ImageColumn("Country")
             })
