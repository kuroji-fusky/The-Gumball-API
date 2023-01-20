FROM python:3-slim-buster

RUN mkdir /api

WORKDIR /api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=80"]