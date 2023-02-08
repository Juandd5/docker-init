FROM python:3.10.8-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt update && \
    apt install -y --no-install-recommends gcc && \
    apt install -y libpq-dev python3-dev && \
    apt clean && rm -rf /var/lib/apt/lists/*

# RUN addgroup -s django && \
    # adduser -s -G django django

COPY requirements.txt /app

RUN python -m pip install -r requirements.txt

COPY . /app

RUN chown -R django /app

USER django

WORKDIR /app
