import pika
import pymongo
import json
import requests
import time

time.sleep(30)  

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq'))

channel = connection.channel()

channel.queue_declare(queue='health_check')


client = pymongo.MongoClient('mongodb://mongo:27017/')
db = client['student_db']
collection = db['students']


def health_check(ch, method, properties, body):
    # Publish a message to the health-check-queue
    # channel = connection.channel()
    print(f"Received message: {body.decode()} from health_check queue")
    response = requests.get(body.decode())
    print(f"Response status code: {response.status_code}")
    ch.basic_ack(delivery_tag=method.delivery_tag)
    channel.basic_publish(exchange='microservices-exchange', routing_key='health_check', body='RabbitMQ is healthy!')
    connection.close()
    return 'OK'




# import pika


# connection = pika.BlockingConnection(
#     pika.ConnectionParameters(host='rabbitmq'))
# channel = connection.channel()

# channel.queue_declare(queue='health_check', durable=True)

# def callback(ch, method, properties, body):
#     print(f"Received message: {body.decode()} from health_check queue")
#     response = requests.get(body.decode())
#     print(f"Response status code: {response.status_code}")
#     ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='health_check', on_message_callback=health_check)

print('Waiting for messages...')
channel.start_consuming()