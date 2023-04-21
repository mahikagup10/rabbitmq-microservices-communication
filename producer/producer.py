from flask import Flask, request
import pika
import json
import time

time.sleep(30)  

app = Flask(__name__)


connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))



# Connect to RabbitMQ
# connection = pika.BlockingConnection(
#     pika.ConnectionParameters(host='rabbitmq', port=5672))
channel = connection.channel()

# Create health_check queue
# channel.queue_declare(queue='health_check', durable=True)

# # Create insert_record queue
# channel.queue_declare(queue='insert_record', durable=True)

# # Create delete_record queue
# channel.queue_declare(queue='delete_record', durable=True)

# # Create read_database queue
# channel.queue_declare(queue='read_database', durable=True)

# Publish message to RabbitMQ
def publish(queue_name, message):
    channel.basic_publish(exchange='',
                          routing_key=queue_name,
                          body=json.dumps(message),
                          properties=pika.BasicProperties(
                              delivery_mode=2,  # make message persistent
                          ))
    print(f"Sent {message} to queue {queue_name}")


# Endpoint to perform health check on a consumer
@app.route('/health_check', methods=['POST'])
def health_check():
    data = request.json
    consumer_name = data['consumer_name']
    message = {'action': 'health_check'}
    publish(consumer_name, message)
    return 'Message sent to consumer'


# Endpoint to insert a record into the database
@app.route('/insert_record', methods=['POST'])
def insert_record():
    data = request.json
    message = {'action': 'insert_record', 'data': data}
    publish('insert_record', message)
    return 'Record inserted'


# Endpoint to delete a record from the database
@app.route('/delete_record', methods=['POST'])
def delete_record():
    data = request.json
    srn = data['srn']
    message = {'action': 'delete_record', 'srn': srn}
    publish('delete_record', message)
    return 'Record deleted'


# Endpoint to read all records from the database
@app.route('/read_database', methods=['POST'])
def read_database():
    message = {'action': 'read_database'}
    publish('read_database', message)
    return 'Message sent to consumer'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)



# import pika

# # Establish a connection to RabbitMQ
# credentials = pika.PlainCredentials('rabbitmquser', 'rabbitmqpassword')
# parameters = pika.ConnectionParameters('rabbitmq', 5672, '/', credentials)
# connection = pika.BlockingConnection(parameters)

# # Create a channel
# channel = connection.channel()

# # Declare an exchange
# channel.exchange_declare(exchange='microservices-exchange', exchange_type='direct')

# # Declare queues
# channel.queue_declare(queue='health-check-queue')
# channel.queue_declare(queue='insertion-queue')
# channel.queue_declare(queue='read-queue')
# channel.queue_declare(queue='deletion-queue')

# # Bind queues to the exchange
# channel.queue_bind(queue='health-check-queue', exchange='microservices-exchange', routing_key='health_check')
# channel.queue_bind(queue='insertion-queue', exchange='microservices-exchange', routing_key='insert_record')
# channel.queue_bind(queue='read-queue', exchange='microservices-exchange', routing_key='read_database')
# channel.queue_bind(queue='deletion-queue', exchange='microservices-exchange', routing_key='delete_record')

# # Close the connection
# connection.close()