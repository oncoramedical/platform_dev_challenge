FROM python:3.8-slim

ENV PROJECT_DIR /app/api
ENV PYTHONPATH=${PROJECT_DIR}
ENV PYTHONDONTWRITEBYTECODE 1
ENV PORT=5000

EXPOSE ${PORT}
WORKDIR ${PROJECT_DIR}

COPY Pipfile Pipfile.lock ${PROJECT_DIR}/

RUN pip install pipenv && \
    pipenv install --system --deploy
