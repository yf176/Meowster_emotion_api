from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

model_name = "j-hartmann/emotion-english-distilroberta-base"
emotion_analyzer = pipeline("text-classification", model=model_name, return_all_scores=True)

class TextRequest(BaseModel):
    text: str

@app.post("/analyze_emotion")
async def analyze_emotion(request: TextRequest):
    results = emotion_analyzer(request.text)
    return {"emotion_vector": results}