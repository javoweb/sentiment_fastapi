<p align = "center" draggable=”false” ><img src="https://user-images.githubusercontent.com/4565451/168209649-f8cb40d1-8de0-4cbe-894a-aa2217ee59b3.png"
     width="200px"
     height="auto"/>
</p>



In-a-rush Sentiment Analysis service using [Hugging Face](https://huggingface.co/) 🤗 and [FastAPI](https://fastapi.tiangolo.com/). The model used is a Bert-based sentiment analysis [model](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english). 🧠

# Installation

## Using Docker

Install [Docker](https://docs.docker.com/engine/install/) 🐳

Build the docker image:

```bash

docker build -t sentiment-container .
```

Run the docker container with the service. The container might take some time to download the models before starting serving.

```bash
docker run -dp 8000:8000 sentiment-container
```

## Locally

Install [conda](https://anaconda.cloud/support-center/installers) and [pytorch](https://pytorch.org/get-started/locally/) accordingly to your OS and hardware

Create the environment

```bash
conda create -n sentiment_analysis python=3.8 pip
```

Activate the environment

```bash
conda activate sentiment_analysis
```

Install requirements

```bash
pip install -r requirements.txt
```

Run the server

```bash
cd src
uvicorn main:app --port 8000
```

# Usage

To know more about other endpoints, consult the OpenAPI documentation in http://127.0.0.1:8000/redoc or try out the swagger interactive documentation in http://127.0.0.1:8000/docs

* **Sentiment analysis endpoint**

## Request

|||
| --- | --- |
| Method | POST |
| Path | /sentiment |
| Body |<code>{"query_string": "String"}</code> |

## Response

| Code | Body | Description |
| --- | --- | --- |
| 200 | <code>{"label": "Sentiment label", "score": "Sentiment score(confidence)"}</code> | Response with the sentiment label `POSITIVE`, `NEGATIVE` and confidence level |
| 422 | <code>{"detail": {"loc": [], "msg": "Message", "type": "Type"}}</code> | Validation error with calidation error details. |


## Sending request using curl

Replace the `query_string` parameter with the sentence you want to

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/sentiment' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "query_string": "You are my best friend"
}'
```
You will get a response similar to the following

```json
{
  "label": "POSITIVE",
  "score": 0.9998573064804077
}
```
