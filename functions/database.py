#In this file, we will be saving the recent conversations that we want to feed to ChatGPT

import json
import random

#Get recent messages function:
def get_recent_messages():
    
    #Defining the file name and learn instruction:
    file_name = "stored_data.json"
    learn_instruction = {
        "role" : "system" , 
        #Here in the content part, we have basically done prompt engineering
        "content" : "You are a compassionate mental‑health peer‑support assistant named Rachel. "
        "Your goal is to listen, validate feelings, and offer practical, evidence‑based coping tips. "
        "Speak with warmth, empathy, and unconditional positive regard — like a caring friend who genuinely wants the best for the user. "
        "Keep each response under 80 words, speak in warm, conversational English, "
        "and always encourage the user to seek professional help if they mention self‑harm or severe distress.."
    }
    
    #Initializing messages i.e. what we eventually want to feed into chatGPT
    messages = []
    
    # #Adding a random element:
    # x = random.uniform(0 , 1)
    # if x < 0.5:
    #     learn_instruction["content"] = learn_instruction["content"] + " All your response will include some dark offensive humour."
    # else:
    #     learn_instruction["content"] = learn_instruction["content"] + " Your response will include a rather concerning questions."
    
    #Append instruction to message:
    messages.append(learn_instruction)
    
    #Get last messages:
    try:
        with open(file_name) as user_file:
            data = json.load(user_file)

            #Append last 5 items of data:
            if data:
                if len(data) < 5:
                    for item in data:
                        messages.append(item) 
                else:
                    for item in data[-5:]:
                        messages.append(item)
    except Exception as e:
        print(e)
        pass   
    
    #Return messages:
    return messages   

#Storing messages 
def store_messages(request_message , response_message):
    
    #Defining the file name:
    file_name = "stored_data.json"
    
    #Getting recent messages:
    messages = get_recent_messages()[1:]
    
    #Adding messages to data:
    user_message = {"role" : "user" , "content" : request_message}
    assistant_message = {"role" : "user" , "content" : response_message}
    messages.append(user_message)
    messages.append(assistant_message)
    
    #Saving the updated file:
    with open(file_name , "w") as f:
        json.dump(messages , f)
        


#Resetting messages:
def reset_messages():
    #Overwriting the file with nothing:
    open("stored_data.json" , "w")