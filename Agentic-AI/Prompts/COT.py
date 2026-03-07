# Chain of Thoughts Prompt

from openai import OpenAI

client = OpenAI(
    api_key='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',
    base_url="https://openrouter.ai/api/v1"
)


SYSTEM_PROMPT = SYSTEM_PROMPT = """
You're an expert AI assistant that solves problems using Chain of Thought reasoning.

You work in three steps:
START → PLAN → OUTPUT

Rules:
- Follow the JSON format strictly
- Only produce one step at a time
- PLAN can appear multiple times
- OUTPUT must contain the final answer

Output JSON format:
{ "step": "START | PLAN | OUTPUT", "content": "string" }

Example:

{ "step": "START", "content": "Hey, can you solve 2 + 3 * 5 / 10?" }

{ "step": "PLAN", "content": "The user is asking to solve a math expression." }

{ "step": "PLAN", "content": "We should apply BODMAS rules." }

{ "step": "PLAN", "content": "First multiply 3 * 5 = 15." }

{ "step": "PLAN", "content": "Now the equation becomes 2 + 15 / 10." }

{ "step": "PLAN", "content": "Divide 15 / 10 = 1.5." }

{ "step": "PLAN", "content": "Now the equation becomes 2 + 1.5." }

{ "step": "PLAN", "content": "Add 2 + 1.5 = 3.5." }

{ "step": "OUTPUT", "content": "3.5" }
"""

response = client.chat.completions.create(
   model="deepseek/deepseek-r1",
   messages=[
       {'role' :"system" , "content":SYSTEM_PROMPT},
       {"role" : "user" , "content" : "Can you write a code to solve find duplicates array [a,b,c,d,a,9,9,c,A,b,A]"}
   ]
)

print(response.choices[0].message.content)