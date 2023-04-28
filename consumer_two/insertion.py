import pika
import time
from flask import Flask, request, jsonify
# from flask_pymongo import PyMongo
import certifi
from pymongo.mongo_client import MongoClient

app = Flask(__name__)

def callback(ch, method, properties, body):
    b = body.decode()
    b = b.split(".")
    dict1 = {"SRN": b[0],"Name":b[1],"Section":b[2]}
    collection.insert_one(dict1)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    return "Student saved successfully!"

# uri = "mongodb+srv://vidisha:vidisha@cc.cybmvzj.mongodb.net/studentdb?retryWrites=true&w=majority"
uri = 'mongodb+srv://charan:charan@cc-project.fgyiawm.mongodb.net/test'
try:
    client = MongoClient(uri,tlsCAFile=certifi.where())
    db = client['studentdb']
    collection = db["student"]
    sleepTime = 20
    time.sleep(sleepTime)
    print('Consumer_two connecting to server ...')
    
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='insert_record', durable=True)
    
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='insert_record', on_message_callback=callback)
    channel.start_consuming()
except Exception as e:
    print(f"Error connecting to MongoDB: {str(e)}")
finally:
    client.close()