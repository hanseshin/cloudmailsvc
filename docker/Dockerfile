FROM python:3.10-slim

WORKDIR /app

COPY flaskBlog /app
COPY docker/requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
