FROM python:3.10.5-slim

WORKDIR /app

ENV PATH="$PATH:/usr/bin/python"

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get remove -y build-essential && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY . .

CMD [ "python", "src/main/app.py" ]
