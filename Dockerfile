# Use official Python image
FROM python:3.9

# Set working directory inside container
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Expose the port your app runs on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
