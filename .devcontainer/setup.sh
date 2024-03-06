#!/bin/bash

# Create a directory for Chromium and Chromedriver if it doesn't exist
mkdir -p chromium
cd chromium

# Download portable Chromium
echo "Downloading Chromium..."
wget -O chromium.zip https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.94/linux64/chrome-headless-shell-linux64.zip
# Unzip and remove the archive
unzip chromium.zip
rm chromium.zip

# Go back to the parent directory
cd ..

# Create a directory for Chromedriver if it doesn't exist
mkdir -p chromedriver
cd chromedriver

# Download Chromedriver
echo "Downloading Chromedriver..."
wget -O chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.94/linux64/chromedriver-linux64.zip
# Unzip and remove the archive
unzip chromedriver.zip
rm chromedriver.zip

# Make chromedriver executable
chmod +x chromedriver

# Go back to the parent directory
cd ..

echo "Setup completed."
