FROM python:3.8-slim-buster

WORKDIR /microservices-rabbitmq/consumer_two

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY insertion.py .

CMD [ "python", "/microservices-rabbitmq/consumer_two/insertion.py" ]
