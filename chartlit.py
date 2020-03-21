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

    chart.add_rows(last_row)
    if(i<20):
        status_text.text('0% Complete')
        progress_bar.progress(0)
    elif i<99:
        status_text.text(f'{i}% Complete')
        progress_bar.progress(i)
    elif i<(len(df1)-2):
        status_text.text('99% Complete')
        progress_bar.progress(99)
    else:
        status_text.text(f'100% Complete')
        progress_bar.progress(100)
    time.sleep(0.07)

progress_bar.empty()


st.button('Restart')
