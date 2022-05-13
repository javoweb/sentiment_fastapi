from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class PredictionRequest(BaseModel):
  query_string: str

sentiment_model = pipeline("sentiment-analysis")

app = FastAPI()

@app.get("/health")
def health():
    return "Service is online."

@app.post("/sentiment")
def sentiment_analysis_endpoint(request: PredictionRequest):
    sentiment_query_sentence = request.query_string
    sentiment = sentiment_model(sentiment_query_sentence)
    return sentiment
