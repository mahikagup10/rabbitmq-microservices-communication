FROM python:3.8-slim-buster

WORKDIR /microservices-rabbitmq/producer

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY producer.py .

CMD [ "python", "/microservices-rabbitmq/producer/producer.py" ]
