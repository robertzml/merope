FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN pip install pymongo APScheduler

EXPOSE 80

COPY ./app /app

WORKDIR /

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]