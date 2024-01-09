import { ReactMediaRecorder } from "react-media-recorder";
import RecordIcon from "./RecordIcon";

type Props = {
    handlesStop : any;
};

function RecordMessage({ handlesStop }: Props) {
    return (
        <ReactMediaRecorder 
            audio 
            onStop={handlesStop} 
            render={({ status, startRecording, stopRecording }) => (
                <div className="mt-2">
                    <button 
                        onMouseDown={startRecording} 
                        onMouseUp={stopRecording} 
                        className="bg-black p-4 rounded-full"
                    >
                        <RecordIcon classText={status == "recording" ? "animate-pulse text-pink-300" : "text-white"} />
                    </button>
                    <p className="mt-2 text-white font-light" >{status}</p>
                </div>
            )}
        />
    );
}

export default RecordMessage;
