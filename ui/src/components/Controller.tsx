import { useState } from "react";
import axios from "axios";
import Title from "./Title";
import RecordMessage from "./RecordMessage";

type ChatMsg = { sender: "me" | "rachel"; blobUrl: string };

export default function Controller() {
  const [isLoading, setIsLoading] = useState(false);
  const [messages, setMessages] = useState<ChatMsg[]>([]);

  /* ------------------------------------------------------------------ */
  /** Convert raw bytes to a URL for the <audio> tag. Saves them as WebM. */
  const bytesToUrl = (data: BlobPart) =>
    URL.createObjectURL(new Blob([data], { type: "audio/webm" }));

  /* ------------------------------------------------------------------ */
  /** Called by <RecordMessage> when the user releases the mic button. */
  const handleStop = async (userBlobUrl: string) => {
    setIsLoading(true);

    // 1. show my "me" bubble right away
    setMessages((prev) => [...prev, { sender: "me", blobUrl: userBlobUrl }]);

    try {
      /* 2. download the recorded blob from the object URL */
      const userBlob = await (await fetch(userBlobUrl)).blob();

      /* 3. build multipart form: voice.webm */
      const formData = new FormData();
      formData.append("file", userBlob, "voice.webm");

      /* 4. POST to FastAPI; axios sets multipart headers automatically */
      const { data } = await axios.post(
        "http://localhost:8000/post-audio",
        formData,
        { responseType: "arraybuffer" }
      );

      /* 5. add Rachel's reply bubble & play it */
      const replyUrl = bytesToUrl(data);
      setMessages((prev) => [...prev, { sender: "rachel", blobUrl: replyUrl }]);
      new Audio(replyUrl).play();
    } catch (err) {
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  /* ------------------------------------------------------------------ */
  return (
    <div className="h-screen overflow-y-hidden">
      <Title setMessages={setMessages} />

      <div className="flex flex-col justify-between h-full overflow-y-scroll pb-96">
        {/* Conversation list */}
        <div className="mt-5 px-5">
          {messages.map((m, i) => (
            <div
              key={`${i}-${m.sender}`}
              className={`flex flex-col ${m.sender === "rachel" ? "items-end" : ""}`}
            >
              <div className="mt-4">
                <p
                  className={
                    m.sender === "rachel"
                      ? "text-right mr-2 italic text-pink-900"
                      : "ml-2 italic text-black"
                  }
                >
                  {m.sender}
                </p>
                <audio src={m.blobUrl} controls />
              </div>
            </div>
          ))}

          {!messages.length && !isLoading && (
            <p className="text-center font-light italic mt-10">
              Send Rachel a message...
            </p>
          )}
          {!messages.length && isLoading && (
            <p className="text-center font-light italic mt-10 animate-pulse">
              Gimme a few seconds!
            </p>
          )}
        </div>

        {/* Recorder */}
        <div className="fixed bottom-0 w-full py-6 border-t text-center bg-gradient-to-r from-black to-pink-800 text-white">
          <RecordMessage handlesStop={handleStop} />
        </div>
      </div>
    </div>
  );
}
