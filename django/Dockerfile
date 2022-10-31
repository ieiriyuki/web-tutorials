FROM python:3.10-slim

COPY pyproject.toml pyproject.toml

COPY mysite mysite

RUN pip install -U pip

RUN curl -sSL https://install.python-poetry.org | python3 -

CMD [ "/bin/bash", "-c", "poetry shell" ]
