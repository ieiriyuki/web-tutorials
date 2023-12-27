FROM python:3.11-slim

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN pip install -U pip \
    && pip install poetry \
    && poetry install

COPY . .

CMD [ "poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
