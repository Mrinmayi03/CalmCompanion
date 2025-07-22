# 🌿  Rachel – A Voice‑First Mental‑Health Companion

<p align="center">
  <img src="docs/demo.gif" width="75%" alt="Screen‑capture of Rachel listening and replying with a calming voice">
</p>

Rachel is a full‑stack, **voice‑enabled mental‑health support chatbot**.  
Press & hold the mic button, talk naturally, and Rachel responds in a warm, empathetic tone—powered by OpenAI Whisper, GPT‑3.5‑Turbo, and ElevenLabs text‑to‑speech.

> **❗️ Disclaimer**  
> Rachel is **not a licensed therapist**. She offers peer‑support style suggestions and always encourages professional help for crisis or clinical concerns.

---

## ✨  Why it matters

| Problem | How Rachel helps |
|---------|------------------|
| Many people feel anxious or down after hours, with no one to talk to. | 24 × 7 private, conversation‑based support in a soothing voice. |
| Text‑only chatbots miss tone and nuance. | **Voice input + voice output** captures emotion and fosters connection. |
| Existing apps require heavy infrastructure. | Single‑repo, flat‑file storage; runs locally or on any small VM. |

Potential real‑world uses:

* **Employee well‑being kiosk** – drop into an office lobby tablet.  
* **On‑call peer support** – residents or students speak anonymously at night.  
* **Voice UI showcase** – demo of multimodal OpenAI stack for hackathons / interviews.

---

## 🏗️  Tech stack

| Layer | Technologies |
|-------|--------------|
| Front‑end | React 18 (TypeScript), Vite, TailwindCSS, `react-media-recorder`, Axios |
| Back‑end | FastAPI, Uvicorn, python‑decouple |
| AI / Audio | OpenAI Whisper (STT) · GPT‑3.5‑Turbo (chat) · ElevenLabs TTS |
| Utility | FFmpeg (audio decode), CORS, flat JSON for short‑term memory |

---

## 🚀  Quick start (local)

### 1 · Clone & install

```bash
git clone https://github.com/<your‑handle>/ChatBot.git
cd ChatBot
```

# Python
python -m venv .venv && source .venv/bin/activate   # Windows: .\.venv\Scripts\activate
pip install -r requirements.txt

# Node
cd ui
npm install
2 · Environment variables
Create .env in project root:

dotenv
Copy
Edit
OPEN_API_KEY=sk-...
OPEN_API_ORG=          # leave blank if using personal account
ELEVEN_API=eleven-...
(Keep .env out of Git; .env.example shows placeholders.)

3 · Run
bash
Copy
Edit
# back‑end (root)
uvicorn main:app --reload

# front‑end (ui/)
npm run dev
Open http://localhost:5173 → allow mic → speak → hear Rachel reply.
