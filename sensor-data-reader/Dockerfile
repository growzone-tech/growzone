FROM python:3 AS builder

WORKDIR /build
RUN pip install --no-cache-dir build
COPY pkg/ /build
RUN python -m build --wheel

FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV MQTT_HOST="localhost"
ENV MQTT_PORT="1883"

WORKDIR /etc/app

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    gcc \
    libc6-dev \
    piod \
    libgpiod-dev
RUN rm -rf /var/lib/apt/lists/*

COPY --from=builder /build/dist/*.whl .
RUN pip install --no-cache-dir *.whl
RUN rm *.whl

CMD ["sensor-data-reader"]