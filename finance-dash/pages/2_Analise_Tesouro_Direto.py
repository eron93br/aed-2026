import pandas as pd
import streamlit as st
import plotly.express as px
from bcb import currency, sgs
import datetime

st.write("Pagina de Analise")

@st.cache_data(ttl=3600)  # Cache for 1 hour
def load_ntnb_data():
    return pd.read_excel('data/NTN-B_Principal_2024.xls')

with st.container():
    st.write("analise do tesouro direto")
    df = load_ntnb_data()
    col1, col2 = st.columns(2)

    with col1: 
        st.write("Taxa Venda Manhã")
        fig_selic = px.line(df, y='Unnamed: 2', title='Taxa Venda Manhã')
        fig_selic.update_layout(height=400)
        st.plotly_chart(fig_selic, use_container_width=True)

    with col2: 
        st.write("PU Compra Manhã")
        fig_selic = px.line(df, y='Unnamed: 3', title='PU Compra Manhã')
        fig_selic.update_layout(height=400)
        st.plotly_chart(fig_selic, use_container_width=True)

    fig_selic = px.line(df, y='Unnamed: 4', title='Taxa Venda Manhã')
    fig_selic.update_layout(height=400)
    st.plotly_chart(fig_selic, use_container_width=True)