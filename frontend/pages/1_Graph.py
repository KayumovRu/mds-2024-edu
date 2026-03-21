import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config("Синусоида", layout='wide')

st.title("Синусоида")

st.sidebar.caption("Я в сайдбаре")

if "delta" not in st.session_state:
    st.session_state["delta"] = 5

st.session_state["delta"] = st.slider("Delta", 1, 10, st.session_state["delta"])

x = np.linspace(0, 10, 100)
y = np.sin(x) + st.session_state["delta"]

df = pd.DataFrame({
    'x':x,
    'sin(x)':y
})

col_1, col_2 = st.columns(2)
with col_2:
    st.line_chart(df.set_index(x)['sin(x)'])
    st.subheader("Все будет хорошо")

debug_expander = st.expander("DEBUG")

with debug_expander:
    st.text(st.session_state)



