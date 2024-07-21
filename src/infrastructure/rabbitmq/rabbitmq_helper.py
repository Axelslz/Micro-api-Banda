import json
import pika
from src.infrastructure.rabbitmq.rabbitmq_config import connect_rabbitmq

def send_to_rabbitmq(queue_name, message):
    connection, channel = connect_rabbitmq()
    try:
        channel.queue_declare(queue=queue_name, durable=True)
        channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            )
        )
        print(f"Mensaje enviado a la cola {queue_name}: {json.dumps(message)}")
    finally:
        connection.close()
