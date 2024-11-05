# LangGraph Agent for MongoDB Project

## API

Run with `project_name run` and access http://127.0.0.1:8000/docs

![](https://raw.githubusercontent.com/rochacbruno/fastapi-project-template/master/docs/api.png)

**For some api calls you must authenticate** using the user created with `project_name create-user`.

### As environment variables

```bash
export PROJECT_NAME_KEY=value
export PROJECT_NAME_KEY="@int 42"
export PROJECT_NAME_KEY="@jinja {{ this.db.uri }}"
export PROJECT_NAME_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

<p align="center">
	<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
    <img src="https://img.shields.io/badge/langchain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white"/>
	<img src="https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white"/>
  <img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white"/>
</p>
