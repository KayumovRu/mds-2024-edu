import requests
import streamlit as st

st.set_page_config(page_title="ML via FastAPI", layout='wide')

data_path = st.text_input("Путь к данным", value="data/Iris.csv")
model_name = st.text_input("Название модели", value="model_1")
train_size = st.slider("Размер выборки для обучения", 0.5, 0.9, 0.7)
max_iter = st.slider("Макс. итераций", 50, 300, 150)

if st.button("Train"):

    payload = {
        "data_path": data_path,
        "model_name": model_name,
        "train_size": train_size,
        "max_iter": max_iter
        }
    
    responce = requests.post(
        "http://127.0.0.1:8000/train_task",
        json=payload,
        timeout=10
    )

    result = responce.json()

    st.info(result["message"])

    st.write("Имя модели", result["model_name"])
    st.write("train_size", result["train_size"])
    # st.write("model_score", result["model_score"])
