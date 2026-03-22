FROM python:3.11-slim AS base

LABEL maintainer="VibeCodingLabs <vibe.coding.inc@gmail.com>"
LABEL description="Phantom Adversarial — AI Red Team Automation Framework"

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# System deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Python deps
COPY pyproject.toml .
RUN pip install --upgrade pip && \
    pip install .

# App code
COPY . .

# Data dirs
RUN mkdir -p /app/data/results /app/data/seeds /app/data/arcanum /app/prompts/generated

ENTRYPOINT ["phantom"]
CMD ["--help"]
