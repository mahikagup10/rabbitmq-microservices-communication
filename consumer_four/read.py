import pika
import pymongo
import time

time.sleep(30)  

# RabbitMQ connection details
RMQ_HOST = "rabbitmq"
RMQ_PORT = 5672
RMQ_USER = "guest"
RMQ_PASS = "guest"

# MongoDB connection details
MONGO_HOST = "mongodb"
MONGO_PORT = 27017
MONGO_DB = "student_db"
MONGO_COLLECTION = "students"

# Create a connection with RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=RMQ_HOST,
        port=RMQ_PORT,
        credentials=pika.PlainCredentials(RMQ_USER, RMQ_PASS),
    )
)
channel = connection.channel()

# Create a connection with MongoDB
client = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]

# Declare the queue
channel.queue_declare(queue="read_database")


# Callback function to process messages
def read_database(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")

    # Retrieve all records from the collection
    records = collection.find()
    print("All records in the database:")
    for record in records:
        print(record)


# Consume messages from the queue
channel.basic_consume(queue="read_database", on_message_callback=read_database, auto_ack=True)

print(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()