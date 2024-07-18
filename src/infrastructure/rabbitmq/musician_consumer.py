import pika
import json
from rabbitmq_config import connect_rabbitmq

def process_message(ch, method, properties, body):
    print("Mensaje recibido:", body)
    message = json.loads(body)
    # Procesar la lógica del mensaje aquí
    response = {"status": "success", "data": "Procesado correctamente"}
    print("Respuesta enviada:", response)
    # Aquí puedes publicar la respuesta en otra cola si es necesario

def start_consumer():
    connection, channel = connect_rabbitmq()
    queue = 'musician_requests'
    channel.queue_declare(queue=queue, durable=True)
    
    channel.basic_consume(queue=queue, on_message_callback=process_message, auto_ack=True)
    print('Esperando mensajes. Para salir presiona CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    start_consumer()
