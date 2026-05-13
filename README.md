# AI Voice Assistant

A production-oriented AI Voice Assistant pipeline built using Whisper, FastAPI, and Llama 3 via Ollama.

This system accepts voice input, performs speech-to-text transcription using Whisper, processes the transcription through a local LLM pipeline, and generates contextual AI responses.

---

## Features

* Speech-to-Text using OpenAI Whisper
* Conversational AI responses using Llama 3
* FastAPI backend APIs
* Local LLM inference via Ollama
* Audio upload and processing pipeline
* Modular AI system architecture

---

## Tech Stack

* Python
* FastAPI
* Whisper
* Ollama
* Llama 3
* FAISS (upcoming)
* Streamlit (upcoming)

---

## System Architecture

```text
Voice Input
    ↓
Whisper Speech-to-Text
    ↓
Llama 3 via Ollama
    ↓
AI Response Generation
    ↓
JSON API Output
```

---

## API Endpoint

### POST `/transcribe`

Upload an audio file and receive:

* speech transcription
* AI-generated response

### Example Response

```json
{
  "transcription": "Hello how are you",
  "response": "I'm doing well! How can I help you today?"
}
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/ai-voice-assistant.git
cd ai-voice-assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

---

## Swagger API Docs

```text
http://127.0.0.1:8000/docs
```

---

## Upcoming Improvements

* Retrieval-Augmented Generation (RAG)
* Voice Output (TTS)
* AI Agents
* Multilingual Support
* Real-Time Streaming
* Docker Deployment

---

## Author

Haris Faheem
AI / LLM Engineer
