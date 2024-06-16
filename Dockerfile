FROM python:3.10.14-slim-bullseye AS builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

COPY pyproject.toml poetry.lock ./

RUN python -m pip install --no-cache-dir poetry==1.8.2 \
    && poetry export --without-hashes --without dev -f requirements.txt -o requirements.txt

FROM python:3.10.14-slim-bullseye

WORKDIR /app

COPY --from=builder requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt

RUN set -ex \
    && addgroup --system --gid 1001 appgroup \
    && adduser --system --uid 1001 --gid 1001 --no-create-home appuser \
    && pip install -r requirements.txt \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN chown -R 1001:1001 /app/
RUN chmod 755 /app/

USER appuser

CMD alembic upgrade head && python3 main.py
