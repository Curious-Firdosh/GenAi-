from openai import OpenAI
from dotenv import load_dotenv
import os
import requests


load_dotenv()

client = OpenAI(api_key=os.getenv("openai_key"))


def get_wether(city : str):
    
    url = f'https://wttr.in/{city}?format=%C+%t'
    response = requests.get(url)
    
    if response.status_code == 200 :
        return f'The Wether in {city} is {response.text}';
    
    return f"Somthing went Wrong"

def main():
    user_query = input('>> ')
    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[
            { "role" : "user" , "content" : user_query}
        ]
    )
    
    print(f"🤖 : {response.choices[0].message.content}")

print(get_wether('indore'))
