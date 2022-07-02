FROM python:3.9-alpine
WORKDIR /code/server
RUN apk add --no-cache --virtual .tmp musl-dev linux-headers openssl-dev g++
COPY requirements.txt requirements.txt
COPY asgi.py asgi.py
RUN pip install -r requirements.txt
RUN apk del .tmp
EXPOSE 5000
COPY ./logs ./logs
COPY ./db ./db
COPY ./src ./src
CMD ["python3", "asgi.py"]