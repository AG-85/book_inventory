# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY src//book_inventory/app.py .

CMD ["python", "app.py"]
