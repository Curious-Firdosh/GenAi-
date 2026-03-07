
# ! Zero Shot Prompting 

#  @ directly giving Instruction To The Model

from openai import OpenAI


client = OpenAI(

    # base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT ="""You Are An Agent name FewShotAi Who Answer Only Realted to Ai Questions. if the query is not related to ai then just say sorry and dont answer that

EXAMPLES:
Q:can you add 1+2
A:Sorry..tell your name and what you are able too
Q:What is Gen ai ?
A: ANSWER IT IN FEW WORDS

"""

response = client.chat.completions.create(
   model="gpt-3.5-turbo",
   messages=[
       {'role' :"system" , "content":SYSTEM_PROMPT},
       {"role" : "user" , "content" : "what is ml"}
   ]
)

print(response.choices[0].message.content)