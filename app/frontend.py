import streamlit as st
import requests
import tempfile
import streamlit.components.v1 as components
from streamlit_mic_recorder import mic_recorder
import time

# PAGE CONFIG
st.set_page_config(
    page_title="AI Voice Assistant",
    page_icon="🎤",
    layout="centered"
)

# CUSTOM CSS
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a, #111827);
        color: white;
    }

    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 700;
        color: white;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        text-align: center;
        color: #94a3b8;
        margin-bottom: 2rem;
    }

    .chat-user {
        background: rgba(59,130,246,0.15);
        padding: 1rem;
        border-radius: 18px;
        margin-bottom: 1rem;
        border: 1px solid rgba(59,130,246,0.25);
        backdrop-filter: blur(10px);
    }

    .chat-ai {
        background: rgba(16,185,129,0.15);
        padding: 1rem;
        border-radius: 18px;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(16,185,129,0.25);
        backdrop-filter: blur(10px);
    }

    .status-box {
        text-align: center;
        padding: 0.8rem;
        border-radius: 12px;
        background: rgba(255,255,255,0.05);
        margin-bottom: 1rem;
        color: #cbd5e1;
    }

    .footer {
        text-align: center;
        color: #64748b;
        margin-top: 3rem;
        font-size: 0.9rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# TITLE
st.markdown('<div class="main-title">AI Voice Assistant</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Whisper + Llama 3 + FastAPI + Streamlit</div>',
    unsafe_allow_html=True
)

# SESSION STATE
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "processing" not in st.session_state:
    st.session_state.processing = False

# STATUS
st.markdown(
    '<div class="status-box">🎙️ Click below and start speaking</div>',
    unsafe_allow_html=True
)

# MIC RECORDER
audio = mic_recorder(
    start_prompt="🎤 Start Recording",
    stop_prompt="⏹️ Stop Recording",
    just_once=True,
    use_container_width=True
)

# PROCESS AUDIO
if audio:

    st.session_state.processing = True

    with st.spinner("⚡ Processing your voice..."):

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            temp_audio.write(audio["bytes"])
            temp_audio_path = temp_audio.name

        with open(temp_audio_path, "rb") as f:

            files = {
                "file": f
            }

            response = requests.post(
                "http://127.0.0.1:8000/transcribe",
                files=files
            )

        data = response.json()

        user_text = data["transcription"]
        ai_text = data["response"]

        st.session_state.chat_history.append({
            "user": user_text,
            "assistant": ai_text
        })

        st.session_state.processing = False

# DISPLAY CHAT HISTORY
for chat in reversed(st.session_state.chat_history):

    st.markdown(
        f'''
        <div class="chat-user">
        <b>🧑 You:</b><br>{chat["user"]}
        </div>
        ''',
        unsafe_allow_html=True
    )

    st.markdown(
        f'''
        <div class="chat-ai">
        <b>🤖 Assistant:</b><br>{chat["assistant"]}
        </div>
        ''',
        unsafe_allow_html=True
    )

# AUTO SPEAK LAST RESPONSE
if st.session_state.chat_history:

    latest_response = st.session_state.chat_history[-1]["assistant"]

    clean_text = (
        latest_response
        .replace("\n", " ")
        .replace("\"", "")
        .replace("'", "")
    )

    components.html(
        f"""
        <script>
        const synth = window.speechSynthesis;

        function speakText() {{

            synth.cancel();

            const utterance = new SpeechSynthesisUtterance(`{clean_text}`);

            utterance.rate = 1;
            utterance.pitch = 1;
            utterance.volume = 1;
            utterance.lang = 'en-US';

            synth.speak(utterance);
        }}

        speakText();
        </script>
        """,
        height=0,
    )

# FOOTER
st.markdown(
    '<div class="footer">Built with Whisper • Ollama • Llama 3 • FastAPI</div>',
    unsafe_allow_html=True
)