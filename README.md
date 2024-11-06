<p align="center">
	<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
    <img src="https://img.shields.io/badge/langchain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white"/>
	<img src="https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white"/>
  <img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white"/>
</p>

# LangGraph Agent for MongoDB Project

LangGraph is a powerful tool designed to manage the LLM agents by inroducing graph structure between different stages(Nodes) of the pipeline.

This agent helps MongoDB for efficient retrieval in natural language.

The idea is that the user nows the type of information in the DB and instead of using SQL, NoSQL queries, asks agent in natural language, than the agent does the search.

## Structure of the Graph

## API

Run with `project_name run` and access http://127.0.0.1:8000/docs

![](https://raw.githubusercontent.com/rochacbruno/fastapi-project-template/master/docs/api.png)

**For some api calls you must authenticate** using the user created with `project_name create-user`.

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

## Installation

```bash
# Clone the repository
git clone https://github.com/DzmitryPihulski/LangGraph-agent-on-MongoDB
cd LangGraph-agent-on-MongoDB

# Install dependencies
pip install -r requirements.txt
```
