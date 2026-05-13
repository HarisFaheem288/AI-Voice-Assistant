# AI Voice Assistant

A production-oriented Voice-to-Voice AI Assistant built using Whisper, FastAPI, Llama 3, and Text-to-Speech synthesis.

The system captures real-time microphone input from the browser, converts speech into text using Whisper, processes the query through a local LLM pipeline via Ollama, and generates contextual AI responses with both text and voice output.

---

## Features

* Real-time browser microphone input
* Speech-to-Text using OpenAI Whisper
* Conversational AI responses using Llama 3
* AI-generated voice responses (TTS)
* FastAPI backend APIs
* Local LLM inference via Ollama
* Real-time voice processing pipeline
* Modular AI system architecture
* Low-latency conversational interaction

---

## Tech Stack

* Python
* FastAPI
* Whisper
* Ollama
* Llama 3
* Text-to-Speech (TTS)
* Streamlit
* PyTorch

---

## System Workflow Architecture

```text id="s2v9hc"
Browser Microphone Input
            ↓
FastAPI Backend API
            ↓
Audio Stream Processing
            ↓
Whisper Speech-to-Text Model
            ↓
Transcribed User Query
            ↓
Llama 3 via Ollama
            ↓
Contextual AI Response
            ↓
Text-to-Speech Synthesis
            ↓
AI Voice Response Output
```

---

## How The System Works

1. The user interacts with the application using browser microphone access.
2. Audio input is captured and sent to the FastAPI backend.
3. The backend processes the audio stream and forwards it to the Whisper model.
4. Whisper converts speech into text transcription.
5. The transcribed query is passed to the locally running Llama 3 model via Ollama.
6. Llama 3 generates a contextual conversational response.
7. The generated response is converted into speech using Text-to-Speech synthesis.
8. The system returns both text and AI-generated voice responses in real time.

---

## Example Workflow

```text id="0yjlwm"
Voice Input:
"Hello, how are you?"

↓ Speech-to-Text

Transcription:
"Hello, how are you?"

↓ LLM Processing

AI Response:
"I'm doing well! How can I assist you today?"

↓ Text-to-Speech

AI Voice Output Generated
```

---

## API Endpoint

### POST `/transcribe`

Processes microphone audio input and returns:

* speech transcription
* AI-generated text response
* AI-generated voice response

---

## Example Response

```json id="jlwmv2"
{
  "transcription": "Hello how are you",
  "response": "I'm doing well! How can I help you today?"
}
```

---

## Project Structure

```text id="jlwmv3"
ai-voice-assistant/
│
├── app/
│   ├── main.py
│   ├── stt/
│   ├── llm/
│   ├── tts/
│   └── frontend/
│
├── uploads/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### Clone Repository

```bash id="jlwmv4"
git clone https://github.com/yourusername/ai-voice-assistant.git
cd ai-voice-assistant
```

---

### Create Virtual Environment

```bash id="jlwmv5"
python -m venv venv
```

---

### Activate Environment

#### Windows

```bash id="jlwmv6"
venv\Scripts\activate
```

#### Linux / Mac

```bash id="jlwmv7"
source venv/bin/activate
```

---

### Install Dependencies

```bash id="jlwmv8"
pip install -r requirements.txt
```

---

## Install Ollama

Download and install Ollama:

[Ollama](https://ollama.com/download?utm_source=chatgpt.com)

Run Llama 3 locally:

```bash id="jlwmv9"
ollama run llama3
```

---

## Run FastAPI Server

```bash id="jlwmva"
uvicorn app.main:app --reload
```

---

## Swagger API Documentation

```text id="jlwmvb"
http://127.0.0.1:8000/docs
```

---

## Future Improvements

* Retrieval-Augmented Generation (RAG)
* AI Agents & Tool Calling
* Conversation Memory
* Multilingual Support
* Real-Time Streaming
* Docker Deployment
* Vector Database Integration
* Voice Activity Detection (VAD)

---

## Author

*  Haris Faheem
*  AI / LLM Engineer
Haris Faheem
AI / LLM Engineer
