# Set up user with UID 1000 (required for Hugging Face Spaces)
RUN useradd -m -u 1000 user

USER user

ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH \
    PYTHONPATH=/home/user/app

WORKDIR $HOME/app

# Install system dependencies
USER root
RUN apt-get update && apt-get install -y \
    python3-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

USER user

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip
COPY backend/requirements-prod.txt .
RUN pip install --no-cache-dir -r requirements-prod.txt

# Copy application files with correct permissions
COPY --chown=user backend/src src/
COPY --chown=user backend/data data/
COPY --chown=user backend/.env.example .env

# Create chroma_db directory
RUN mkdir -p chroma_db

# Expose port (Hugging Face will use this)
EXPOSE 7860

# Start the FastAPI application
CMD ["uvicorn", "src.rag_chatbot.main:app", "--host", "0.0.0.0", "--port", "7860"]
