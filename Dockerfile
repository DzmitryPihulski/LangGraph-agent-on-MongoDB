FROM python:3.9


WORKDIR /


COPY ./requirements.txt /requirements.txt
COPY ./src/ /


RUN pip install --no-cache-dir --upgrade -r /requirements.txt

CMD uvicorn serve:app --host 0.0.0.0 --port ${APP_PORT}