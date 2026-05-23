from openai import OpenAI
import os
from pydantic import BaseModel, Field
from typing import Optional
import json
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("openai_key")
)


def calculator(expression : str):
    try :
        return eval(expression)
    except Exception as e:
        return f"Error in calculation : {str(e)}"
    
available_Tool = {
      "calculator" :  calculator
 }

SYSTEM_PROMPT = """
   You are an AI Calculator Agent.
   Your task is to solve user math Problem step by step 
   and if any question is not realted to math then tell sorry and tell somthing
   
   Follow Rules Strictly : 
   - only perform one step At  a time 
   - understnad the user problem first 
   -Use Tools When it is necessary
   -allow follow json format
   - if anye question is not related to math then say sorry and tell somthing else and exit the loop after telling one time.
   
   
   
    Output Format :
    { "step" : "START | PLAN | OUTPUT | OBSERVE | TOOL" , "content" : "string" , "tool" : "string" , "input" : "string"}
    
    example 1 -
    USER: Can you solve 2 + 3 * 5 ?
    
    AI->
    START : {"step" : "START" , "content" :"that is the question user aasked let solve it step by step" }
    PLAN:{"step" : "PLAN"  , content : "let see is there sny tool available."}
    PLAN: {"step" : "PlAN" , content : "let's call the calculator tool with input 2 + 3 * 5"}
    PLAN:{"step" : "TOOL" : "tool" : "calculator" , "input" : "2 + 3 * 5" }
    PLAN:{"step" : "OBSERVE","tool" : "calculator" , "output": "the output from the tool is 17 "}
    PLAN:{"step" : "PLAN" , content : "Great, we have solved the problem and the answer is 17"}
    OUTPUT: {"step" : "OUTPUT" , content : "The answer of that question  is 17"}
    
     example 2 -
     If the user's question is not related to math,
    respond directly with OUTPUT step only.

Example:
{
  "step":"OUTPUT",
  "content":"I can only solve math-related problems."
}
        
"""


class MyOutputFormat(BaseModel):
    step : str = Field(...)
    content : Optional[str] 
    input :  Optional[str] 
    tool :  Optional[str] 
    

message_history = [
    { "role" : "system" , "content" : SYSTEM_PROMPT}
]


userQuery = input('>> ')

message_history.append({"role" : 'user' , "content" : userQuery })

while True :
    response = client.chat.completions.parse(
        model='gpt-4.1-nano',
        response_format=MyOutputFormat,
        messages= message_history
    )
    
    raw_result = response.choices[0].message.content
    message_history.append({"role" : "assistant" , "content" : raw_result})
    
    parsed_result = response.choices[0].message.parsed
    
    
    if parsed_result.step == "START" :
        print(parsed_result.content)
        continue
    elif parsed_result.step == "PLAN":
        print(parsed_result.content)
        continue
    elif parsed_result.step == "TOOL":
        tool_call = parsed_result.tool
        tool_input = parsed_result.input
        print (f"⚙️ {tool_call}({tool_input})")
        
        tool_response = available_Tool[tool_call](tool_input)
        print (f"⚙️ {tool_call}({tool_input}) ={tool_response}")
        
        message_history.append(
            {
                "role" : "developer",
                "content" : json.dumps({
                     "step" : "OBSERVE" , "tool" : tool_call , "input" : tool_input , "output" : tool_response
                })
            }
        )
        continue;
    elif parsed_result.step == "OUTPUT" : 
        print(parsed_result.content )
        break 
