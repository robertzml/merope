FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN pip install pymongo APScheduler

EXPOSE 80

COPY ./app /app

WORKDIR /

# SET TIMEZONE
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' >/etc/timezone

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]