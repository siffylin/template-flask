FROM --platform=$BUILDPLATFORM python:3.11-alpine AS builder

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt /app

RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . /app

ENV FLASK_APP=app

ENTRYPOINT ["python3"]
CMD ["app.py"]