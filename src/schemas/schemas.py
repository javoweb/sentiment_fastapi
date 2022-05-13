from pydantic import BaseModel


class PredictionRequest(BaseModel):
    query_string: str


class PredictionResponse(BaseModel):
    label: str
    score: float
