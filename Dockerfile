FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy the source code and data into the container
COPY src/ ./src/
COPY data/ ./data/
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Specify the default command to run the application
CMD ["python", "src/app.py", "src/gradioUI.py"]