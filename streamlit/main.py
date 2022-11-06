import random
import time

import pandas as pd
import streamlit as st


st.write('Here is our first attempt at using data to create a table.')

st.sidebar.markdown("# Main page")
add_selectbox = st.sidebar.selectbox(
    "How would you like?",
    ("Email", "Phone", "Twitter")
)
add_slider = st.sidebar.slider(
    "Select a range of values",
    0.0, 100.0, (25.0, 75.0)
)


df = pd.DataFrame(
    {
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40],
    }
)
df

list_x = [
    [
        random.randint(0, 99) for a in range(10)
    ]
    for b in range(20)
]
dataframe = pd.DataFrame(
    list_x,
    columns=[f"col_{i}" for i in range(10)]
)
st.dataframe(dataframe.style.highlight_max(axis=0))

st.table(dataframe)

chart_data = pd.DataFrame(
    [
        [random.randint(0, 99) for i in range(3)]
        for j in range(20)
    ],
    columns="a,b,c".split(","),
)
st.line_chart(chart_data)

map_data = pd.DataFrame.from_records(
    [
        [random.uniform(35.6, 35.8), random.uniform(138.9, 139.9)]
        for i in range(10)
    ],
    columns=["lat", "lon"],
)
st.map(map_data)

x = st.slider("x")
st.write(x, "squared is", x * x)

st.text_input("your name", key="name")
st.session_state.name

if st.checkbox("show dataframe"):
    data = pd.DataFrame([[1, 2], [1, 3], [2,1]], columns=["a", "b"])
    data

option = st.selectbox(
    "which num?",
    [1, 2, 3, 4],
)
"Selected: ", option

left_column, right_column = st.columns(2)
left_column.button("Press me")
with right_column:
    chosen= st.radio(
        "Sorting hat",
        ("Gryff", "Raven", "Huffle", "Slyth")
    )
    st.write(f"You are in {chosen}")

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(50):
    latest_iteration.text(f"iteration {i + 1}")
    bar.progress(i + 1)
    time.sleep(0.1)


from mymodule import say_foo

word = say_foo()
word

if "shared" not in st.session_state:
    st.session_state["shared"] = True

# eof
