In a rush Sentiment Analysis service using [Hugging Face](https://huggingface.co/) and [FastAPI](https://fastapi.tiangolo.com/)

# Installation

## Using Docker

Install [Docker](https://docs.docker.com/engine/install/)

Build the docker image:

```bash
docker build -t sentiment-container .
```

Run the docker container with the service:

```bash
docker run -dp 8000:8000 sentiment-container
```

## Locally

Install [conda](https://anaconda.cloud/support-center/installers) and [pytorch](https://pytorch.org/get-started/locally/) accordingly to your OS and hardware

Create the environment

```bash
conda create -n sentiment-analysis python=3.8 pip
```

Activate the environment

```bash
conda activate fastapi_env
```

Install requirements

```bash
pip install -r requirements.txt
```

Run the server

```bash
uvicorn main:app --port 8000
```

# Usage

To know how to use the service consult the swagger documentation going to http://127.0.0.1:8000/docs

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
| 200 | <code>[{"label": "Sentiment label", "score": "Sentiment score(confidence)"}]</code> | Response with the sentiment label `POSITIVE`, `NEGATIVE` and confidence level |


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
[
  {
    "label": "POSITIVE",
    "score": 0.9998573064804077
  }
]
```