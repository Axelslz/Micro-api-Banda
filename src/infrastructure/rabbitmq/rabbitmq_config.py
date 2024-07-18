import pika

RABBITMQ_URL = 'amqp://localhost'

def connect_rabbitmq():
    parameters = pika.URLParameters(RABBITMQ_URL)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    return connection, channel
