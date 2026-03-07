from openai import OpenAI

client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


response = client.chat.completions.create(
   model="gemini-3-flash-preview",
   messages=[
       {'role' :"system" , "content":"You Are An Agent Who Answer Only Realted to Ai Questions. if the query is not related to ai then just say sorry and dont answer that"},
       {"role" : "user" , "content" : "add 2+2"}
   ]
)

print(response.choices[0].message.content)