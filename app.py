import streamlit as st
import seaborn as sns
import pandas as pd

st.set_page_config(page_title="Penguins Explorer", page_icon="🐧", layout="wide")

@st.cache_data
def load_data() -> pd.DataFrame:
    """Lazy‑loads Palmer Penguins dataset from seaborn."""
    return sns.load_dataset("penguins").dropna()

st.title("🐧 Penguins Explorer")
st.markdown(
    """
    Dive into the **Palmer Penguins** dataset!
    Use the sidebar (left) to jump between pages:
    1. **Data Explorer** – browse & filter the raw table  
    2. **Interactive Charts** – visualize bill & flipper metrics  
    3. **Predict Species** – tiny ML demo in real time  
    """
)

with st.expander("About this project", expanded=False):
    st.write(
        "Built with Streamlit, Altair, pandas, seaborn and scikit‑learn. "
        "Deployed free on Streamlit Community Cloud."
    )

# A fun Easter egg 🥚
if st.button("Show me a random penguin fact!"):
    st.info("Adélie penguins breed in colonies that can reach **250,000+** individuals.")
