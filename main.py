import streamlit as st

from app.ai_tools import render_ai_tools_page
from app.fruits import render_fruit_page

if __name__ == "__main__":

    st.set_page_config(page_title="Demo App", layout="wide")
    pg = st.navigation([
        st.Page(render_fruit_page, title="Fruits in Asia"), 
        st.Page(render_ai_tools_page, title="AI Tools"),
    ])
    pg.run()
