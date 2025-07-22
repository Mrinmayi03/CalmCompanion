from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

from functions.openai_requests import (
    convert_audio_to_text,
    get_chat_response,
)
from functions.database import store_messages, reset_messages
from functions.text_to_speech import convert_text_to_speech

app = FastAPI()                    # default /docs stays enabled ✔️

ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:4173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health():
    return {"message": "Healthy"}


@app.get("/reset")
async def reset():
    reset_messages()
    return {"message": "Conversation reset."}


@app.post("/post-audio")
async def post_audio(file: UploadFile = File(...)):
    # save upload to disk so Whisper can open it
    with open(file.filename, "wb") as f:
        f.write(file.file.read())

    with open(file.filename, "rb") as f:
        text = convert_audio_to_text(f)
    if not text:
        raise HTTPException(400, "Failed to decode the audio.")

    reply = get_chat_response(text)
    if not reply:
        raise HTTPException(400, "Failed to get the chat response.")

    store_messages(text, reply)

    mp3 = convert_text_to_speech(reply)
    if not mp3:
        raise HTTPException(400, "Failed to get TTS audio.")

    return StreamingResponse(iter([mp3]), media_type="audio/mpeg")
