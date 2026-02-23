# Math API

Simple REST API using FastAPI and Docker.

## Run locally

pip install -r requirements.txt
uvicorn app.main:app --reload

## Run with Docker

docker build -t math-api .
docker run -p 8000:8000 math-api

## Example endpoint

http://localhost:8000/add?a=1&b=2
