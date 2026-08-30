from pathlib import Path
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os 
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore


load_dotenv();


pdf_path = Path(__file__).resolve().parent / "pythonbook.pdf"

# @ Load PDF - pip install -qU pypdf langchain-community

loader = PyPDFLoader(file_path=str(pdf_path))

docs = loader.load()

#!@ Chunking and spliting to the smaller chunks that going to converted to vectors - pip install -qU langchain-text-splitters
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size= 1000,
    chunk_overlap = 400
)

chunks = text_splitter.split_documents(documents=docs)

# @ adding embedding model to convert the  chunks into the vecore embding that representation of the text in the numaricale fomat
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

vectorstore = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333/",
    collection_name = "PythonChatBot"
)

print ("Indexing Of Document Is Done....")