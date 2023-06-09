FROM python:3.11

WORKDIR /app

COPY requirements.txt .
COPY dao.py .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000