FROM python:3.9


WORKDIR /


COPY pyproject.toml pdm.lock* ./
COPY ./src/ /

RUN pip install pdm
RUN pdm install --prod

CMD pdm run uvicorn serve:app --host 0.0.0.0 --port ${APP_PORT} --reload