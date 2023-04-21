import pika
import pymongo
import json
import time

time.sleep(30)  # Add delay of 30 seconds

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='delete_record')

client = pymongo.MongoClient('mongodb://mongo:27017/')
db = client['student_db']
collection = db['students']


def delete_record(ch, method, properties, body):
    srn = body.decode('utf-8')
    collection.delete_one({'srn': srn})
    print(f"Record with SRN {srn} deleted from the database.")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='delete_record', on_message_callback=delete_record)

print('Waiting for delete requests...')
channel.start_consuming()



# import pika
# import pymongo
# import json

# connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
# channel = connection.channel()

# channel.queue_declare(queue='delete_record')

# client = pymongo.MongoClient('mongodb://mongo:27017/')
# db = client['student_db']
# collection = db['students']


# def delete_record(ch, method, properties, body):
#     srn = body.decode('utf-8')
#     collection.delete_one({'srn': srn})
#     print(f"Record with SRN {srn} deleted from the database.")
#     ch.basic_ack(delivery_tag=method.delivery_tag)


# channel.basic_qos(prefetch_count=1)
# channel.basic_consume(queue='delete_record', on_message_callback=delete_record)

# print('Waiting for delete requests...')
# channel.start_consuming()