import streamlit as st
import os
import pandas as pd

input_fpath = "./data/fruits/fruits.csv"
result_fpath = "./results/fruits_results.csv"


def load_data():
    source_df = pd.read_csv(input_fpath)
    if os.path.exists(result_fpath):
        result_df = pd.read_csv(result_fpath)
    else:
        result_df = source_df[['fruit']].copy()
        result_df["completed"] = False

    source_df = source_df.merge(result_df)
    source_df.index.name = 'Id'
    return source_df[["fruit", "image_url", "completed"]]


def render_table():
    def save_result_handle():
        edited_rows = st.session_state['edited_df']['edited_rows']
        fresh_df = st.session_state['data_df']
        result_df = fresh_df[["fruit", "completed"]].copy()
        for k, v in edited_rows.items():
            for col, value in v.items():
                result_df.loc[k, col] = value
        result_df.to_csv(result_fpath, index=False)

    column_config = {
        "fruit": st.column_config.TextColumn("Fruit Name", width=125,),
        "image_url": st.column_config.ImageColumn(
            "Image",
            width=125,
        ),
        "completed": st.column_config.CheckboxColumn("Tried?", width=100),
    }

    st.data_editor(
        st.session_state['data_df'],
        column_config=column_config,
        row_height=75,
        hide_index=True,
        key='edited_df',
        width="content",
        on_change=save_result_handle
    )


def render_fruit_page():
    if 'data_df' not in st.session_state:
        st.session_state['data_df'] = load_data()

    col2, _ = st.columns([7, 3])
    with col2:
        st.subheader("Fruits in Asia")
        render_table()
