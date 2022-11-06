# https://docs.streamlit.io/library/get-started/create-an-app
import os
import random
from os.path import join as pjoin
from os.path import normpath
from typing import List, Optional

import pandas as pd
import streamlit as st


tzoffset = datetime.timedelta(hours=9)
tzoffset

BASE_DIR = os.path.dirname(__file__)
BASE_DIR

@st.cache
def load_data(filepath: str, cols_date: Optional[List[str]]):
    df = pd.read_csv(
        filepath,
        dtype=dict_sample,
    )
    for col in cols_date:
        df[col] = pd.to_datetime(df[col])
    return df

dict_sample = {
    "a": int,
    "b": "string",
    "d": bool,
}

state = st.text("Loading data")
filepath = normpath(pjoin(BASE_DIR, "../data/sample.csv"))
df = load_data(
    filepath,
    ["c"]
)
st.dataframe(df)
state.text("Done (using st.cache)")

st.subheader("number of pickups by hour")

data = [
    random.randint(1, 50) for i in range(10)
]
st.bar_chart(data)

# eof
