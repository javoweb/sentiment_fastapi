from enum import Enum

from pydantic import BaseModel


class SentimentEnum(str, Enum):
    NEGATIVE = "NEGATIVE"
    POSITIVE = "POSITIVE"


class PredictionRequest(BaseModel):
    query_string: str


class PredictionResponse(BaseModel):
    label: SentimentEnum
    score: float
