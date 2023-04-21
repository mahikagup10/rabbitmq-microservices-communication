FROM python:3.8-slim-buster

WORKDIR /microservices-rabbitmq/consumer_one

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY healthcheck.py .

RUN pip install Flask

CMD [ "python", "/microservices-rabbitmq/consumer_one/healthcheck.py" ]
