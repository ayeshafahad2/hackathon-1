FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY backend/requirements-prod.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements-prod.txt

# Copy application files
COPY backend/src ./src/

# Create chroma_db directory (data will be created on first run)
RUN mkdir -p chroma_db

# Expose port
EXPOSE 7860

# Set environment variables
ENV PYTHONPATH=/app

# Start the FastAPI application
CMD ["uvicorn", "src.rag_chatbot.main:app", "--host", "0.0.0.0", "--port", "7860"]
