import streamlit as st


st.markdown("# Prediction")
st.sidebar.markdown("side")

from mymodule import say_foo

word = say_foo()
word

st.write(st.session_state["shared"])
