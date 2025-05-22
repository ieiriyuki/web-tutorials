FROM python:3.11 AS app

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4", "--reload"]

FROM python:3.11 AS client

WORKDIR /client

RUN pip install aiohttp

COPY post.py .

CMD ["python3", "post.py"]
