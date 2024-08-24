import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Comparative Analysis of GHI Profiles in Benin, Sierra Leone, and Togo",
                   page_icon=":bar_chart:",
                   layout="wide"
                   )
st.header('Comparative Analysis of GHI Profiles in Benin, Sierra Leone, and Togo')

@st.cache_data
def load_data(path:str):
    data = pd.read_csv(path)
    return data

data_dir = "./data"
dataframes = {
    "benin": os.path.join(data_dir, "benin-malanville.csv"),
    "sierra_leone": os.path.join(data_dir, "sierraleone-bumbuna.csv"),
    "togo": os.path.join(data_dir, "togo-dapaong_qc.csv"),
}

# Load and display the line charts for all three countries
for name, file_path in dataframes.items():
    df = load_data(file_path).head(10000)
    st.subheader(f"{name.capitalize()} - GHI")
    st.line_chart(df['GHI'])