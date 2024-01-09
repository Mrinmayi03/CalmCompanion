import requests
from decouple import config

ELEVEN_API = config("ELEVEN_API")

#Eleven Labs:
#Convert text to speech:
def convert_text_to_speech(message):
    
    #Defining data/body:
    body = {
        "text" : message , 
        "voice_setting" : {
            "stability" : 0 ,
            "similarity_boost" : 0,
        }
    }
    
    #Defining voice:
    voice_rachel = "21m00Tcm4TlvDq8ikWAM"
    
    headers = {"xi-api-key" : ELEVEN_API , "Content-Type" : "application/json" , "accept" : "audio/mpeg" }
    
    #Constructing URL(API Endpoint):
    endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_rachel}"
    
    
    #Send requests:
    try:
        response = requests.post(endpoint , json = body , headers = headers)
    
    except Exception as e:
        return
    
    
    #Handling response:
    if response.status_code == 200:
        return response.content
    else:
        return