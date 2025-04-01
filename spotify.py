import streamlit as st
import pandas as pd

st.set_page_config (
    page_title="Musicas do Spotify",
    page_icon="🎵",
    layout="wide",
)
dataFrame = pd.read_csv("data/spotify.csv")

dataFrame.set_index("Track", inplace=True)


artists= dataFrame["Artist"].value_counts().index

artist = st.selectbox("Artista",artists)
dataFilter = dataFrame[dataFrame["Artist"] == artist]

albuns = dataFilter["Album"].value_counts().index
album = st.selectbox("Album",albuns)

dataFilterAlbum = dataFrame[dataFrame["Album"] == album]



display = st.checkbox("Mostrar detalhes da música")
if display:
    st.write("Detalhes do Artista Escolhido")
    st.bar_chart(dataFilterAlbum["Stream"])

