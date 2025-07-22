import requests
from decouple import config

ELEVEN_API = config("ELEVEN_API")                 
VOICE_ID = "21m00Tcm4TlvDq8ikWAM"                 


def convert_text_to_speech(message: str):
    body = {
        "text": message,
        "voice_setting": {"stability": 0, "similarity_boost": 0},
    }
    headers = {
        "xi-api-key": ELEVEN_API,
        "Content-Type": "application/json",
        "accept": "audio/mpeg",
    }
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    try:
        resp = requests.post(url, json=body, headers=headers, timeout=30)
        if resp.status_code == 200:
            return resp.content
    except Exception:
        pass
    return None
