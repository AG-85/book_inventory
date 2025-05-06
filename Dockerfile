# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY src//book_inventory/inventory.py .

CMD ["python", "app.py"]
