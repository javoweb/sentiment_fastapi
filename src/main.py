from fastapi import FastAPI

from models.models import sentiment_model
from schemas.schemas import PredictionRequest, PredictionResponse

app = FastAPI()


@app.get("/health", response_model=str)
def health() -> str:
    return "Service is online."


@app.post("/sentiment", response_model=PredictionResponse)
def sentiment_analysis_endpoint(request: PredictionRequest) -> PredictionResponse:
    sentiment_query_sentence = request.query_string
    sentiment = sentiment_model(sentiment_query_sentence)
    return sentiment[0]
