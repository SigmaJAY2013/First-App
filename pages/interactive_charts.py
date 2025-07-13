import streamlit as st
import altair as alt
import pandas as pd

from app import load_data

st.header("📊 Interactive Charts")

df = load_data()

numerics = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
x = st.selectbox("X‑axis", numerics, index=0)
y = st.selectbox("Y‑axis", numerics, index=1)

chart = (
    alt.Chart(df)
    .mark_circle(size=80, opacity=0.7)
    .encode(
        x=alt.X(f"{x}:Q", title=x.replace("_", " ").capitalize()),
        y=alt.Y(f"{y}:Q", title=y.replace("_", " ").capitalize()),
        color="species",
        tooltip=["species", x, y, "island"],
    )
    .interactive()
)

st.altair_chart(chart, use_container_width=True)

