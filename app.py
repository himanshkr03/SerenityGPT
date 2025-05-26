# app.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Enable CORS for Streamlit to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

LLAMA_API_URL = "http://127.0.0.1:8080/completion"  # llamafile server

@app.post("/")
async def root(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    try:
        llama_response = requests.post(
            LLAMA_API_URL,
            json={"prompt": prompt, "temperature": 0.7, "n_predict": 300},
            timeout=60
        )
        result = llama_response.json()
        return {"response": result.get("content", "No response from LLaMA.")}
    except Exception as e:
        return {"response": f"❌ Failed to connect to LLaMA: {str(e)}"}
