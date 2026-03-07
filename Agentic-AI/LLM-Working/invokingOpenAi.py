from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()


response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role" : "user" , "content" : "What is Gen ai Explain in 20 words "}
    ]
)

# response = client.responses.create(
#     model="chatgpt-4o-latest",
#     input="What is Gen-ai explain in 20 words "
# )

print("Result:", response.choices[0].message.content)