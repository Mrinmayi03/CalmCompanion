import { useState } from 'react';
import axios from "axios";

type Props = {
    setMessages : any;
}

function Title( {setMessages} : Props) {
    const [isResetting , setIsResetting] = useState(false);

    //Function to reset the conversation:
    const resetConversation = async () => {
        setIsResetting(true);

        await axios.get("http://localhost:8000/reset").then((res) => {
            if (res.status == 200) {
                //alert(res.data);
                setMessages([])
        
            }
            else{
                console.error("There was an error with the API request to the backend.")
            }
        }).catch((err) => {
            console.error(err.message);
        }
        )
        setIsResetting(false);
    }


    return <div className="flex justify-between items-center w-full p4 bg-pink-900 text-black font-bold shadow">
        <div className="italic">Rachel</div>
        <button onClick={resetConversation} className={"transition-all duration-300 text-black hover:text-pink-400 " + (isResetting && "animate-pulse")}>
            <svg 
                xmlns="http://www.w3.org/2000/svg" 
                fill="none" 
                viewBox="0 0 24 24" 
                strokeWidth={1.5} 
                stroke="currentColor" 
                className="w-6 h-6"
            >
                <path 
                    strokeLinecap="round" 
                    strokeLinejoin="round" 
                    d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0 3.181 3.183a8.25 8.25 0 0 0 13.803-3.7M4.031 9.865a8.25 8.25 0 0 1 13.803-3.7l3.181 3.182m0-4.991v4.99" 
                />
            </svg>
        </button>
    </div>

}

export default Title;