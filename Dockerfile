# Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY src/book_inventory/inventory.py .

CMD ["python3", "inventory.py"]
