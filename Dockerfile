# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

EXPOSE 8000

WORKDIR /app

# Install system dependencies
RUN apk update
RUN apk add \
    pkconfig \
    gcc \
    musl-dev \
    bash \
    mariadb-dev

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /urs/src/app
COPY . /app

# Run server
ENTRYPOINT ["python3"]

CMD ["manage.py", "runserver", "0.0.0.0:8000"]