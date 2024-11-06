<p align="center">
	<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
    <img src="https://img.shields.io/badge/langchain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white"/>
	<img src="https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white"/>
  <img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white"/>
</p>

# LangGraph Agent for MongoDB

LangGraph is a powerful tool designed to manage the LLM agents by inroducing graph structure between different stages(Nodes) of the pipeline.

This agent helps MongoDB for efficient retrieval in natural language.

The idea is that the user nows the type of information in the DB and instead of using SQL, NoSQL queries, asks agent in natural language, than the agent does the search.

## Structure of the Graph

1. The user asks the question at the `__start__`
2. The question is preprocessed in the `Input Validator`
3. `Exploration Node` creates query to the `MongoDB`
4. The query is executed in the `MongoDB` node.
5. User gets the answer at the `__end__`

<p align="center">
  <img src="data/structure.jpeg" alt="Structure" style="border: 10px solid #22a2b6;">
</p>

## As environment variables

`.env`

```python
MONGO_PORT = 27017
MONGO_HOST = localhost

APP_PORT = 1234
MONGO_LOGIN = '' # for example 'root'
MONGO_PASSWORD = '' # for example 'example'
```

`src/.env`

```python
MISTRAL_API_KEY = '' # get yours from mistral webpage
MONGO_PORT = 27017
MONGO_HOST = localhost
MONGO_DB_NAME = "AirBnB"
MONGO_COLLECTION_NAME = "AirBnB"
MONGO_LOGIN = '' # for example 'root'
MONGO_PASSWORD = '' # for example 'example'
```

## API

Run with `docker compose up -d --build` and access http://127.0.0.1:1234/docs

![](data/image.png)

## Installation

```bash
# Clone the repository
git clone https://github.com/DzmitryPihulski/LangGraph-agent-on-MongoDB
cd LangGraph-agent-on-MongoDB

# Install dependencies
pip install -r requirements.txt

# Run docker network with
docker compose up -d --build
```
