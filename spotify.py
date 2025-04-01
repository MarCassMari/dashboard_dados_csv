import streamlit as st
import pandas as pd


dataFrame = pd.read_csv("data/spotify.csv")
dataFrame.set_index("Artist", inplace=True)

st.line_chart(dataFrame[dataFrame["Stream"]> 1000000000]["Stream"])
