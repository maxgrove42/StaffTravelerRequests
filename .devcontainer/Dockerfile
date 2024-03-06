# Start with a Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install essential packages needed for the setup script and general operation.
# This might include tools like wget or unzip if your setup.sh script uses them.
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Copy your project files into the container
COPY . /app

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make setup.sh executable and run it to install Chromium and ChromeDriver
RUN chmod +x setup.sh && ./setup.sh
