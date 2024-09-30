import streamlit as st
import pandas as pd
# import plotly.express as px

st.set_page_config(layout="wide")
df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
# df["Date"] = pd.to_datetime(df["Date"])

print("ola")