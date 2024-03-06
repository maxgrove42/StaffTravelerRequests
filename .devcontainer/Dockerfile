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

# Copy the requirements.txt file into the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project files into the container
COPY . .

# Run setup.sh to install Chromium and ChromeDriver
RUN chmod +x setup.sh && ./setup.sh
