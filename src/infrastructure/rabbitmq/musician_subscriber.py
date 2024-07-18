from src.infrastructure.rabbitmq.rabbitmq_config import connect_rabbitmq

def start_musician_subscriber():
    connection, channel = connect_rabbitmq()
    queue = 'musician_created'
    channel.queue_declare(queue=queue, durable=True)

    def callback(ch, method, properties, body):
        print(f"Mensaje recibido de la cola {queue}: {body}")
        # Procesar el mensaje aquí

    channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)
    print('Esperando mensajes. Para salir presiona CTRL+C')
    channel.start_consuming()
