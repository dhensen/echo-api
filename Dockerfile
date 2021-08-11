FROM python:3.9.2-alpine3.13

ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
RUN apk add --no-cache build-base libffi-dev libressl-dev musl-dev

RUN mkdir /app
RUN python -m pip install poetry

COPY pyproject.toml /app
WORKDIR /app

RUN poetry install --no-dev

COPY localhost.crt /app
COPY localhost.key /app
COPY api.py /app


EXPOSE 8443

CMD ["poetry", "run", "python3", "-m", "api"]
