import pika
import json
import pymongo
import time

time.sleep(30)  

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='insert_record', durable=True)


mongo_url = "mongodb://localhost:27017/"
mongo_client = pymongo.MongoClient(mongo_url)
mongo_db = mongo_client["student_db"]
mongo_collection = mongo_db["students"]

    

def insert_record(ch, method, properties, body):
    print(f" [x] Received {body}")
    data = json.loads(body)
    mongo_collection.insert_one(data)
    print(" [x] Record inserted successfully")
    ch.basic_ack(delivery_tag=method.delivery_tag)

    

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='insert_record', on_message_callback=insert_record)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

