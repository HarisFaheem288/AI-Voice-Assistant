from app.llm.chatbot import generate_response
from app.tts.speaker import text_to_speech
from fastapi import FastAPI, UploadFile, File
import os

from app.stt.transcriber import transcribe_audio

app = FastAPI()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def home():
    return {"message": "AI Voice Assistant Running"}

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    text = transcribe_audio(file_path)

    ai_response = generate_response(text)

    audio_file = text_to_speech(ai_response)

    return {
       "transcription": text,
       "response": ai_response,
           }
