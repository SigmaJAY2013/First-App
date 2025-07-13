import streamlit as st
import pandas as pd

from app import load_data

st.header("🕵️‍♂️ Data Explorer")

df = load_data()

# Sidebar filters
with st.sidebar:
    st.subheader("Filters")
    species = st.multiselect("Species", df["species"].unique(), default=list(df["species"].unique()))
    island = st.multiselect("Island", df["island"].unique(), default=list(df["island"].unique()))

mask = df["species"].isin(species) & df["island"].isin(island)
st.write(f"Showing **{mask.sum()}** of {len(df)} rows")
st.dataframe(df[mask], use_container_width=True)

