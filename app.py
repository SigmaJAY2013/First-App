import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Hello Streamlit!", page_icon="👋")

# --- Sidebar ---
st.sidebar.title("About")
st.sidebar.markdown(
    """
    **This is your first Streamlit app!**

    - Built with pure Python ✨  
    - Runs for free on the Streamlit Community Cloud  
    - Ready to fork, edit and deploy  
    """
)

# --- Main area ---
st.title("👋 Hello, World!")
st.write(
    """
    Welcome to your very first Streamlit application.

    - Edit *app.py*, commit, and watch the app update automatically.  
    - Use the sidebar to add more pages or controls.  
    """
)

name = st.text_input("What’s your name?")
if name:
    st.success(f"Nice to meet you, **{name}**!")

st.markdown("---")
st.caption(f"Rendered at {datetime.utcnow():%Y‑%m‑%d %H:%M UTC}")
