import streamlit as st

from config.constants import APP_TITLE, APP_ICON


def setup_page() -> None:
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon=APP_ICON,
        layout="centered",
    )
