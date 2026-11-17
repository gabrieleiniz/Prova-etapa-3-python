import pandas as pd
import streamlit as st 

df = pd.read_csv("dados_transport_bh.csv", sep = ";")
df.columns = df.columns.str.strip()
df["LINHA"] = df["LINHA"].astype(str).str.strip()
df = df[~df["PC"].isin ([0,3])]
viagens = df.groupby("LINHA").size().reset_index(name="viagens")

df_filtrado = df[(df["VIAGENS", 10])]

st.title("Titulo painel")
st.header("Título painel")
st.sidebar("Título painel")
tabela = st.dataframe[10]

st.set_page_config(page_title="linha", layout="wide")
st.title("Título painel")
df = pd.read_csv("dados.csv")
opcao = st.sidebar.radio(
 "Selecione a visualização:",
 ["Tabela", "Gráficos"]
)
if opcao == "linha":
 st.header("Título painel", layout = "horizontal")
 st.dataframe(df, use_container_width=True)
elif opcao == "Gráficos":
 st.header("Título painel", layout = "vertical")
 st.write("dados_transporte_bh.csv")