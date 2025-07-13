import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

from app import load_data

st.header("🔮 Predict Penguin Species")

df = load_data()
X = df[["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]]
y = df["species"]
model = LogisticRegression(max_iter=1000, multi_class="multinomial").fit(X, y)

st.subheader("Enter measurements")
bill_length = st.slider("Bill length (mm)", 30.0, 60.0, 45.0)
bill_depth  = st.slider("Bill depth (mm)", 13.0, 21.0, 17.0)
flipper_len = st.slider("Flipper length (mm)", 170, 235, 200)
body_mass   = st.slider("Body mass (g)", 2700, 6300, 4000)

sample = np.array([[bill_length, bill_depth, flipper_len, body_mass]])
pred = model.predict(sample)[0]
proba = model.predict_proba(sample).max()

st.success(f"**Predicted species:** {pred}  \n(Probability {proba:.0%})")

