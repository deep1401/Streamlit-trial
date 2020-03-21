import time
import streamlit as st
from vega_datasets import data

progress_bar=st.sidebar.progress(0)
status_text=st.sidebar.empty()
df=data.barley()
df1=df[['yield','year']]
chart=st.line_chart([float(df1['year'][0]),float(df1['yield'][0])])


for i in range(len(df1)):
    last_row=[float(df1['year'][i]),float(df1['yield'][i])]
    status_text.text(f'{i}% Complete')
    chart.add_rows(last_row)
    progress_bar.progress(int((i/len(df1))*100))
    time.sleep(0.07)

progress_bar.empty()


st.button('Restart')
