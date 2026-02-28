import pandas as pd
import streamlit as st
import plotly.express as px
from bcb import currency, sgs
import datetime

# Configure page FIRST for better performance
st.set_page_config(layout="wide", page_title="Dashboard Financeiro")

# ------ codigo de cores do dashboard ----
blue_palette = [
    "#071D3D", "#102E5E", "#1E4A8A", "#2E63A8", "#3E79C2",
    "#5590D8", "#6FA5E6", "#8AB8EE", "#A9C9F2", "#C5D7F5", "#D9D9D9"
]

LISTA_MOEDAS = ['USD', 'EUR', 'GBP', 'CHF', 'CAD']
today = datetime.datetime.now()
fixed_year = 2024
jan_1 = datetime.date(fixed_year, 1, 1)
dec_31 = datetime.date(fixed_year, 12, 31)

# ----- Cached data loaders --------
@st.cache_data(ttl=3600)  # Cache for 1 hour
def load_moto_data():
    return pd.read_csv('data/Motos.csv')

@st.cache_data(ttl=3600)
def load_currency_data(start_date, end_date):
    return currency.get(LISTA_MOEDAS, start=start_date, end=end_date)

@st.cache_data(ttl=3600)
def load_selic_data(start_date, end_date):
    return sgs.get({'SELIC': 1178}, start=start_date, end=end_date)

@st.cache_data(ttl=3600)
def load_ipca_data(start_date, end_date):
    return sgs.get({'IPCA': 433}, start=start_date, end=end_date)

# Sidebar
with st.sidebar:
    st.write("Selecionar a janela temporal")
    start_date, end_date = st.date_input(
        "Selecione o intervalo da analise:",
        (jan_1, datetime.date(fixed_year, 1, 7)),
        jan_1,
        dec_31,
        format="YYYY.MM.DD",
    )

# Load data
mdf = load_moto_data()
moedas = load_currency_data(start_date, end_date)
selic = load_selic_data(start_date, end_date)
ipca = load_ipca_data(start_date, end_date)

# UI
st.title("Dashboard Financeiro")

st.header("Análise Macro - Brasil 🇧🇷")
col1, col2 = st.columns(2)
#tab1, tab2 = st.tabs(["SELIC", "IPCA"])

with col1:
#with tab1:
    if not selic.empty:
        fig_selic = px.line(selic, y='SELIC', title='Taxa de Juros no Brasil (SELIC)')
        fig_selic.update_layout(height=400)
        st.plotly_chart(fig_selic, use_container_width=True)

with col2:
#with tab2:
    if not ipca.empty:
        fig_ipca = px.line(ipca, y='IPCA', title='Variacao Mensal do IPCA')
        fig_ipca.update_layout(height=400)
        st.plotly_chart(fig_ipca, use_container_width=True)

st.header("Variação de Moedas")
moeda_sel = st.pills("Selecione a(s) moeda(s) desejada:", LISTA_MOEDAS, selection_mode="multi")

if moeda_sel:
    if not moedas.empty:
        fig_dolar = px.line(moedas, y=moeda_sel, title=f'Variação de {", ".join(moeda_sel)}/BRL')
        fig_dolar.update_layout(height=400)
        st.plotly_chart(fig_dolar, use_container_width=True)

st.header("Vendas de Motos")
col1, col2 = st.columns([3, 1])

with st.container():
    with col1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg", width='stretch')

    with col2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")
