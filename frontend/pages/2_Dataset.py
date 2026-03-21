import streamlit as st
import pandas as pd

st.set_page_config("Датасет", layout='wide')

st.title("Датасет")

@st.cache_data(ttl=10)
def load_data():
    df = pd.read_csv("data/Iris.csv")
    print("Загрузил снова...")
    return df

df = load_data()

species_options = df["Species"].unique()

select_species = st.selectbox(
    "Выберите класс",
    options=species_options,
    label_visibility='collapsed',
    index=None
)

filtred_df = df[df["Species"] == select_species]

if st.button("PASS"):
    pass

st.dataframe(filtred_df)