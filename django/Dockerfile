FROM python:3.10-slim

WORKDIR /app

ENV POETRY_HOME="/opt/poetry"
ENV POETRY_VERSION="1.2.2"
ENV PATH="${POETRY_HOME}/venv/bin:$PATH"

COPY install.python-poetry.py install.python-poetry.py

RUN python3 install.python-poetry.py

COPY pyproject.toml pyproject.toml

COPY mysite mysite

WORKDIR /app/mysite

ARG INSTALL_OPTION
RUN poetry install ${INSTALL_OPTION}

CMD ["/bin/bash"]
