from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI( 
                title="Web Data Extraction API",
                description="API for converting and extracting structured web data"
            )

@app.get('/')
def health():
    return {
        "message" : "Welcome to The Web Data Extraction Project "
    }