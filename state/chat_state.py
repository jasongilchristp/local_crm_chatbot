from typing import Literal, TypedDict

import streamlit as st

Role = Literal["user", "assistant"]


class ChatMessage(TypedDict):
    role: Role
    content: str


def init_chat_state() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = []


def get_messages() -> list[ChatMessage]:
    return st.session_state.messages


def add_message(role: Role, content: str) -> None:
    st.session_state.messages.append({"role": role, "content": content})


def clear_messages() -> None:
    st.session_state.messages = []
