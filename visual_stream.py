import streamlit as st
import pandas as pd
import numpy as np

import plotly.figure_factory as ff
import matplotlib.pyplot as plt
st.title("Jinica")

@st.cache
def load_data(nrows):
    data = pd.read_csv('lyrics-JINA - Sheet1.csv', nrows=nrows)
    df = pd.read_csv('df.csv', nrows=nrows)
 
    return data
    # return df
  

    data_load_state = st.text('Loading data...')


songs = load_data(30)
st.subheader("SIP SIP HURRAYYYY!!")
st.write(songs)

st.bar_chart(songs["Song"])

# st.line_chart(df,"count")
#Bar Chart
# st.bar_chart(songs["Song"])
# plt.scatter(Singer, Song)
# plt.xlabel("Singers")
# plt.ylabel("Songs")
# plt.title(" Visualzation")
# plt.show()