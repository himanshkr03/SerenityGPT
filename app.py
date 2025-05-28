from fastapi import FastAPI, Request
from pydantic import BaseModel
import requests

app = FastAPI()

MODEL_API_URL = "http://127.0.0.1:8080/completion"
API_KEY = "llamakey"  # <-- Your API key from Anaconda Navigator

class PromptRequest(BaseModel):
    model: str
    prompt: str

@app.post("/")
def get_ai_response(data: PromptRequest):
    payload = {
        "prompt": data.prompt,
        "temperature": 0.7,
        "max_tokens": 256
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",  # Include the API key
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(MODEL_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        completion = response.json().get("content", "") or response.json().get("response", "")
        return {"response": completion}
    except Exception as e:
        return {"response": f"Error: {e}"}
