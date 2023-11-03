# Use the official Python image as the base image
FROM python:3.9

# Set environment variables for Python (recommended for Docker)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install -r requirements.txt

# Copy the entire project into the container
COPY . /app/