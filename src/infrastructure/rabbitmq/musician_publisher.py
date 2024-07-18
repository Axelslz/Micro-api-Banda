import pika
from src.infrastructure.rabbitmq.rabbitmq_config import connect_rabbitmq

def publish_musician_created(musician):
    connection, channel = connect_rabbitmq()
    queue = 'musician_created'
    channel.queue_declare(queue=queue, durable=True)
    channel.basic_publish(
        exchange='',
        routing_key=queue,
        body=str(musician),
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        )
    )
    print(f"Mensaje enviado a la cola {queue}: {musician}")
    connection.close()
