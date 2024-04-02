FROM python:3.11-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUBUFFERED 1

# Install enviornment dependencies
RUN apk update \
    && apk add --no-cache --virtual .build-deps \
        gcc \
        libc-dev \
        linux-headers \
        musl-dev \
        postgresql-dev \
        libffi-dev \
        jpeg-dev \
        zlib-dev \
    && apk add --no-cache \
        libpq \
        jpeg \
        zlib \
    && apk add --update --no-cache sqlite

# Set the working directory
WORKDIR /app/

# Install python dependencies
COPY ./requirements.txt ./requirements.txt
RUN python3 -m pip install --upgrade pip \
    && python3 -m pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . /app/

