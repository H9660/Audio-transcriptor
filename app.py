from fastapi import FastAPI, UploadFile, File
import speech_recognition as sr
import tempfile

app = FastAPI()

@app.post("/transcribe")
async def transcribe(audio: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(await audio.read())
        tmp.flush()

        recognizer = sr.Recognizer()
        with sr.AudioFile(tmp.name) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)

    return {"transcription": text}
