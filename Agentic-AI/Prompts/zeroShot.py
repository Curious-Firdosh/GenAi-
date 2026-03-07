
# ! Zero Shot Prompting 

#  @ directly giving Instruction To The Model

from openai import OpenAI


client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT ="You Are An Agent name ZeroShot Who Answer Only Realted to Ai Questions. if the query is not related to ai then just say sorry and dont answer that"

response = client.chat.completions.create(
   model="gemini-3-flash-preview",
   messages=[
       {'role' :"system" , "content":SYSTEM_PROMPT},
       {"role" : "user" , "content" : "add 2+2"}
   ]
)

print(response.choices[0].message.content)