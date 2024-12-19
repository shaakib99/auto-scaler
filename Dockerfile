FROM ubuntu:22.04

WORKDIR /app

COPY  . .

ENV DEBIAN_FRONTEND=noninteractive

# Update and install dependencies
RUN apt-get update && apt-get install -y \
    software-properties-common \
    libmysqlclient-dev \
    pkg-config \
    build-essential \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update && apt-get install -y \
    python3.11 python3.11-venv python3-pip tzdata \
    && rm -rf /var/lib/apt/lists/*

RUN pip install  -r  requirements.txt


# CMD [ "opentelemetry-instrument","--service_name=host_server", "--metrics_exporter=otlp", "--traces_exporter=otlp", "fastapi", "dev" ]
CMD ["fastapi", "run", "--host=0.0.0.0", "--port=8000" ]
