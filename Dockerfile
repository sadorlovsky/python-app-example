FROM python:3.7-alpine
WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apk add --no-cache --virtual .build-deps make gcc musl-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps make gcc musl-dev

COPY . .

CMD ["python", "./main.py"]
