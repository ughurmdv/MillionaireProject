FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir --disable-pip-version-check -r requirements.txt


COPY backend/ .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
