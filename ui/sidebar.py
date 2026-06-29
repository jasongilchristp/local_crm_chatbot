from dataclasses import dataclass

import streamlit as st

from config.constants import DEFAULT_MODELS


@dataclass
class SidebarSettings:
    model: str
    temperature: float
    system_prompt: str
    clear_chat: bool


def render_sidebar(default_system_prompt: str) -> SidebarSettings:
    with st.sidebar:
        st.title("⚙️ Settings")

        model = st.selectbox(
            "Choose Ollama Model",
            DEFAULT_MODELS,
            index=0,
        )

        temperature = st.slider(
            "Temperature/Creativity",
            min_value=0.0,
            max_value=1.0,
            value=0.5,
            step=0.1,
            help="0 = Minimal Creativity, 1 = Maximum Creativity",
        )

        system_prompt = st.text_area(
            "System Prompt",
            value=default_system_prompt,
            height=280,
        )

        clear_chat = st.button("Clear Chat")

        st.markdown("---")
        st.markdown("### Teaching Notes")
        st.markdown("- No API key required")
        st.markdown("- Ollama runs models locally")

    return SidebarSettings(
        model=model,
        temperature=temperature,
        system_prompt=system_prompt,
        clear_chat=clear_chat,
    )
