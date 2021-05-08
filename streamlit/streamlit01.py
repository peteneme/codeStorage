#!/usr/bin/python
import yfinance as yf
import streamlit as st
import pandas as pd
import numpy

st.write("""
# H1
## H2
### H3
*Italic text*


https://docs.streamlit.io/en/stable/api.html
""")


### random table
df1 = pd.DataFrame( numpy.random.randn(50, 20), 
                    columns=('col %d' % i for i in range(20)))

my_table = st.table(df1)


### read data from yf
st.write("""
https://pypi.org/project/yfinance/
""")
tickerData = yf.Ticker("AAPL")
tickerDf = tickerData.history(period='1d', start='2010-1-1', stop='2020-1-1')
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)