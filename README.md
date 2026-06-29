# CRM ChatBot - Modular Streamlit Version

A clean, modular Streamlit chatbot that connects to a local Ollama instance and acts as a Microsoft D365 PowerApps tutor.

## Project structure

```text
ollama_chatbot/
├── app.py
├── README.md
├── requirements.txt
├── config/
│   ├── __init__.py
│   ├── constants.py
│   └── page.py
├── prompts/
│   ├── __init__.py
│   └── system_prompt.py
├── services/
│   ├── __init__.py
│   └── ollama_client.py
├── state/
│   ├── __init__.py
│   └── chat_state.py
├── ui/
│   ├── __init__.py
│   ├── chat.py
│   ├── header.py
│   ├── sidebar.py
│   └── styles.py
└── utils/
    └── __init__.py
```

## Why this structure

- `app.py` is the orchestrator and stays small.
- `config/` keeps constants and page setup separate from business logic.
- `prompts/` stores long prompt text outside the UI flow.
- `services/` contains Ollama communication logic.
- `state/` wraps `st.session_state` so chat memory is easy to manage.
- `ui/` holds reusable Streamlit rendering functions.

## Setup

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate it

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start Ollama

```bash
ollama serve
```

### 5. Pull at least one model

```bash
ollama pull phi4-mini:latest
```

You can also pull any model listed in the sidebar.

### 6. Run the app

```bash
streamlit run app.py
```
