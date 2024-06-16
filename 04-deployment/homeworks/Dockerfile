# Use the base image with the model and vectorizer
FROM agrigorev/zoomcamp-model:mlops-2024-3.10.13-slim

# If you have any dependencies in a requirements.txt file, copy that in as well
COPY requirements.txt .

# Install any required packages
RUN pip install --no-cache-dir -r requirements.txt

# Set work directory
WORKDIR /app

# Create the output/yellow directory
RUN mkdir -p output/yellow

# Copy your script into the container
COPY starter.py .

# Run script
CMD [ "python", "starter.py", "yellow", "2023", "5" ]