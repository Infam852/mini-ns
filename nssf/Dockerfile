# syntax=docker/dockerfile:1
FROM python:3.9-slim-buster

WORKDIR /code
ENV FLASK_APP=nssf/app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5001
COPY . .

CMD ["flask", "run", "--port=5001"]