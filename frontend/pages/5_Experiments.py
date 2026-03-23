import streamlit as st
import requests
import pandas as pd

st.header("История экспериментов")

if st.button("Обновить историю"):
   try:
       response = requests.get("http://127.0.0.1:8000/experiments")

       if response.status_code == 200:
           data = response.json()

           if data:
               df = pd.DataFrame(data)
               st.dataframe(df)
           else:
               st.info("Пока нет экспериментов")

       else:
           st.error("Ошибка при получении данных")

   except Exception as e:
       st.error("Ошибка подключения")
       st.write(e)
