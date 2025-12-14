import streamlit as st

from fruits import render_fruit_page

if __name__ == "__main__":
    st.set_page_config(page_title="Asian Fruits", layout="wide")
    render_fruit_page()
