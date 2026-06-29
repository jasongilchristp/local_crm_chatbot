import requests
import streamlit as st

from config.page import setup_page
from config.constants import CHAT_INPUT_PLACEHOLDER
from prompts.system_prompt import DEFAULT_SYSTEM_PROMPT
from services.ollama_client import is_ollama_running, build_payload, stream_chat
from state.chat_state import init_chat_state, get_messages, add_message, clear_messages
from ui.styles import inject_styles
from ui.header import render_header
from ui.sidebar import render_sidebar
from ui.chat import render_chat_history


def main() -> None:
    setup_page()
    inject_styles()
    render_header()

    init_chat_state()
    settings = render_sidebar(DEFAULT_SYSTEM_PROMPT)

    if settings.clear_chat:
        clear_messages()
        st.rerun()

    if not is_ollama_running():
        st.error("Ollama is not running. Please open a terminal and run: ollama serve")
        st.info(f"Then pull the model using: ollama pull {settings.model}")
        st.stop()

    render_chat_history(get_messages())

    user_prompt = st.chat_input(CHAT_INPUT_PLACEHOLDER)
    if not user_prompt:
        return

    add_message("user", user_prompt)

    with st.chat_message("user"):
        st.markdown(user_prompt)

    payload = build_payload(
        model=settings.model,
        system_prompt=settings.system_prompt,
        temperature=settings.temperature,
        messages=get_messages(),
    )

    full_response = ""

    with st.chat_message("assistant"):
        placeholder = st.empty()

        try:
            for chunk in stream_chat(payload):
                full_response += chunk
                placeholder.markdown(full_response + "▌")

            placeholder.markdown(full_response)

        except requests.exceptions.HTTPError as e:
            full_response = (
                f"HTTP Error: {str(e)}\n\n"
                f"Most likely the model '{settings.model}' is not downloaded.\n\n"
                f"Run this command in terminal:\n\n"
                f"ollama pull {settings.model}"
            )
            placeholder.error(full_response)

        except Exception as e:
            full_response = f"Error: {str(e)}"
            placeholder.error(full_response)

    add_message("assistant", full_response)


if __name__ == "__main__":
    main()
