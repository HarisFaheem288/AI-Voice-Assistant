from gtts import gTTS
import uuid
import os

OUTPUT_FOLDER = "outputs"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def text_to_speech(text: str):

    filename = f"{uuid.uuid4()}.mp3"

    filepath = os.path.join(OUTPUT_FOLDER, filename)

    tts = gTTS(text=text, lang='en')

    tts.save(filepath)

    return filepath