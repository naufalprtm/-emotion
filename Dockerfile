# Use a slim version of Python 3.9 as a base image
FROM python:3.9-slim

# Set environment variables to avoid Python buffering
ENV PYTHONUNBUFFERED 1

# Install system dependencies and Python packages
RUN apt-get update && apt-get install -y \
    python3-opencv \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy the project files
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "pyemotion/server.py"]
