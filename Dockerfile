FROM python:3.11-slim
WORKDIR /app
COPY skill_building/backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY skill_building/backend/ .
EXPOSE 8000
CMD ["sh", "-c", "uvicorn main_lightweight:app --host 0.0.0.0 --port $PORT"]
