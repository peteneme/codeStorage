#!/usr/bin/python
import yfinance as yf
import streamlit as st
import pandas as pd
import numpy

### hide hamburger menu and hide bottom streamit link 
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """           
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 




st.title(""" Just some title...
""")


### just place image
st.image('./green.jpg')


st.write("""
https://github.github.com/gfm/
""")
st.markdown('Streamlit is **_really_ cool**.')


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


### some more graphs
st.write("""
More graphs
""")
data = tickerDf.Close
st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)
#st.pyplot(data)
#st.altair_chart(data)
#st.vega_lite_chart(data)
#st.plotly_chart(data)
#st.bokeh_chart(data)
#st.pydeck_chart(data)
#st.deck_gl_chart(data)
#st.graphviz_chart(data)
#st.map(data)


### more playings
st.write("""
https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py
""")

st.button('Hit me')
st.checkbox('Check me out')
st.radio('Radio', [1,2,3])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
slider1 = st.slider('Slide me', min_value=0, max_value=10)
slider2 = st.select_slider('2 options only slide to select', options=[1,'20'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
st.color_picker('Pick a color')

