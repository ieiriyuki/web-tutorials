FROM python:3.10-slim

ENV POETRY_HOME="/opt/poetry"
ENV POETRY_VERSION="1.2.2"
ENV PATH="${POETRY_HOME}/venv/bin:$PATH"

COPY install-poetry.py install-poetry.py

RUN python3 install-poetry.py

WORKDIR /app

COPY . .

RUN poetry install --sync
