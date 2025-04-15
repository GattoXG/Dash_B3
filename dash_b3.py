import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(
    page_title="Painel de Ações da B3",
    page_icon="📈",
    layout="wide"
)

st.header("**Painel de preços de fechamento e dividendos de ações da B3**")

ticker = st.text_input("Digite o ticker da ação:", "PETR4")
empresa = yf.Ticker(f"{ticker}.SA")

tickerDF = empresa.history(
    period="1d",
    start="2019-01-01",
    end="2025-03-31",
)

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.write(f"**Empresa:** {empresa.info['longName']}")
with col2:
    st.write(f"**Mercado:** {empresa.info['industry']}")
with col3:
    st.write(f"**Preço atual:** {empresa.info['currentPrice']}")

st.line_chart(tickerDF['Close'], use_container_width=True)
st.bar_chart(tickerDF['Dividends'], use_container_width=True)