import os
from openai import OpenAI

class GPTConnector:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key == None:
            print("No API key found. Refer to README.md for instructions.")
            exit(0)
            
        # sets the api key from the OPENAI_API_KEY env variable
        self.client = OpenAI()
    
    def ask_gpt(self, prompt):        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        
        # access response string
        response_message = response.choices[0].message.content
        
        print(response_message)
        return response_message
