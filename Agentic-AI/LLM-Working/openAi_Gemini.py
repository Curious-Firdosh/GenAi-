from openai import OpenAI
import json

client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key='AIzaSyB6uKvWxWHlMNkRZrY7_5HCYie-cfReUsY'
);



Prompt = """
    You are a strict JSON response AI.

You MUST follow these rules:

Always return ONLY valid JSON.
Never return text outside JSON.
Never use markdown or explanations.
If the output is not valid JSON, regenerate it until it becomes valid JSON.
 """
 

response = client.chat.completions.create(

    
   model="gemini-3-flash-preview",
   temperature=0.2,
   messages=[
       {'role' :"system" , "content":Prompt},
       {"role" : "user" , "content" : "what is Generative ai ? in simple words and how it helps the Full stack Webdevloper"}
   ]
   
)

# Extract text
output = response.choices[0].message.content


# Convert JSON string → dict
data = json.loads(output)

print(data)

