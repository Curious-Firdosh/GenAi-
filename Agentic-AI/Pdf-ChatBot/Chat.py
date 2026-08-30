from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI


load_dotenv();

client = OpenAI()

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

vector_db = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    url="http://localhost:6333/",
    collection_name = "PythonChatBot"
);

# take user Input
user_query = input('Ask Somthing >>  ')

search_results = vector_db.similarity_search(query=user_query)

context = "\n\n\n".join([f"Page Content: {result.page_content}" for result in search_results])


SYSTEM_PROMPT = """
    YOU ARE AN AI ASSISTANT THAT HELPS THE USER TO ANSWER THE QUESTIONS BASED ON THE CONTEXT RETRIEVED FROM THE PDF FILE ALONG WITH PAGE CONTENT AND PAGE NUMBERS
    YOU  SHOULD ANSWER THE USER BASED ON THE fOLLOWING CONTEXT AND NAVIGATE THE USER TO OPEN RIGHT PAGE NUMBER TO KNOW MOREE--
    {context}
    IF YOU DON'T KNOW THE ANSWER TO THE USER QUESTION, YOU SHOULD SAY "I DON'T KNOW THE ANSWER TO THIS QUESTION".
    YOU SHOULD NOT MAKE UP ANSWERS IF YOU DON'T KNOW THE ANSWER TO THE USER QUESTION
    
    
"""

response = client.chat.completions.create(
    model='gpt-4.1-nano',
    messages=[
        {"role" : "system" , "content" : SYSTEM_PROMPT},
        {"role" : "user" , "content" : user_query} 
    ]
)

print(f"🤖-- {response.choices[0].message.content}")
