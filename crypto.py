import streamlit as st
import yfinance as yf
import pandas as pd


#---Title---
st.title("Coin Data")
st.write("#")

#---Coins---#
coins = ("BTC-USD", "ETH-USD", "USDT-USD", "USDC-USD", 
"BNB-USD", "XRP-USD", "BUSD-USD", "DOGE-USD", "ADA-USD", "SHIB-USD")

#---GUI---#
with st.sidebar:
    st.title("Crypto Dashboard")
    st.write("#")
    choice = st.selectbox("Select Coin", (coins))
    start1 = st.date_input("Graph Start", value=pd.to_datetime("2022-01-01"))
    start = st.date_input("Chart Start", value=pd.to_datetime("2022-12-24"))
    end = st.date_input("End", value=pd.to_datetime("today"))

#---FUNCTIONS---#
def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]

col1, col2 = st.columns(2)

def crypto_code(choice):
    with col1:
        df = yf.download(choice, start1, end)["Adj Close"]
        st.write("#")
        st.write(choice, "is", get_current_price(choice))
        st.line_chart(df)
    with col2:
        st.write("###")
        st.write(yf.download(choice, start, end)["Open"])
        ["Open Data", choice, start, end]

#---CODE---#
while True:
    crypto_code(choice)
    break
