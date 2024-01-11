import os
import time
import re
import pandas as pd
# from openai import OpenAI
import openai

# def chatgpt():
#     openai.api_key = "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"
#     messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]

#     # while True: 
#     message = input("User : ") 
#     if message: 
#         messages.append({"role": "user", "content": message},)
#         chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages) 
        
#     reply = chat.choices[0].message.content 
#     print(f"ChatGPT: {reply}") 
#     messages.append({"role": "assistant", "content": reply})

# chatgpt()



appending = input()
appending = "\""+appending+"\""
emotions_prompt = "Describe the emotion that are shown in lyrics of this song: "
print(emotions_prompt+appending)