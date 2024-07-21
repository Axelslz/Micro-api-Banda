import json
import pika
from src.infrastructure.rabbitmq.rabbitmq_config import connect_rabbitmq

def publish_musician_created(musician):
    connection, channel = connect_rabbitmq()
    try:
        queue = 'musician_created'
        channel.queue_declare(queue=queue, durable=True)
        message = {'musician': musician.to_dict()}
        channel.basic_publish(
            exchange='',
            routing_key=queue,
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            )
        )
        print(f"Mensaje enviado a la cola {queue}: {json.dumps(message)}")
    finally:
        connection.close()

def publish_musician_request(musician_id):
    connection, channel = connect_rabbitmq()
    try:
        queue = 'musician_requests'
        channel.queue_declare(queue=queue, durable=True)
        message = {'musician_id': musician_id}
        channel.basic_publish(
            exchange='',
            routing_key=queue,
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            )
        )
        print(f"Mensaje enviado a la cola {queue}: {json.dumps(message)}")
    finally:
        connection.close()
