import streamlit as st

st.title("Демо")

name = st.text_input("Введите имя")
number = st.slider("Ввведите число", 0, 10, 5)

if st.sidebar.button("Посчитать квадрат"):
    res = number ** 2
    st.info(f"Привет, {name}! Квадрат числа: {res}")
    st.balloons()