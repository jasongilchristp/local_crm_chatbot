import streamlit as st


def render_header() -> None:
    st.markdown(
        """
        <div class="hero-card">
            <div class="brand-title"><span class="accent">Jason Gilchrist P</span></div>
            <div class="brand-subtitle">Microsoft D365 PowerApps Tutor</div>
            <div class="small-note">Microsoft D365 PowerApps — Simply Explained!</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
