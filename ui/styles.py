import streamlit as st

APP_CSS = """
<style>
.block-container {
    max-width: 900px;
    padding-top: 2.5rem;
    font-family: "Segoe UI", sans-serif;
}
.hero-card {
    background: #1f2937;
    border: 1px solid #374151;
    border-radius: 12px;
    padding: 28px;
    margin-bottom: 24px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
}
.brand-title {
    font-size: 28px;
    font-weight: 700;
    color: #f9fafb;
    margin-bottom: 6px;
}
.brand-subtitle {
    font-size: 16px;
    color: #d1d5db;
    font-weight: 500;
}
.accent {
    color: #a855f7;
}
.small-note {
    color: #9ca3af;
    font-size: 13px;
    margin-top: 8px;
}
.stButton button {
    border-radius: 6px;
    background-color: #742774;
    color: #ffffff;
    font-weight: 600;
    border: none;
    padding: 0.6rem 1.2rem;
}
.stButton button:hover {
    background-color: #9333ea;
}
</style>
"""


def inject_styles() -> None:
    st.markdown(APP_CSS, unsafe_allow_html=True)
