# Dockerfile

# Pull base image
FROM python:3.7

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DATABASE_URL postgres://postgres:postgres@db:5432/labs_store

# Set work directory
WORKDIR /app

# Install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --dev

# Copy project
COPY . /app/