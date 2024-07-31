import sys
import os

# Agregar el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

import json
import pika
from flask import Flask
from src.infrastructure.database.mysql.connection import db, init_db
from src.infrastructure.repositories.musician_repository import MusicianRepositoryImpl
from src.infrastructure.rabbitmq.rabbitmq_config import connect_rabbitmq

app = Flask(__name__)
init_db(app)

repository = MusicianRepositoryImpl()

def process_message(ch, method, properties, body):
    message = json.loads(body)
    musician_id = message.get('musician_id')
    
    with app.app_context():
        if musician_id:
            repository.record_profile_visit(musician_id)
            print(f"Visita registrada para el músico con ID {musician_id}")
            
            # Obtener estadísticas de visitas
            visits = repository.get_profile_visits(musician_id)
            
            response_message = {
                'musician_id': musician_id,
                'visits': visits
            }
            
            # Enviar respuesta a RabbitMQ
            connection, channel = connect_rabbitmq()
            try:
                channel.queue_declare(queue='profile_visit_stats_responses', durable=True)
                channel.basic_publish(
                    exchange='',
                    routing_key='profile_visit_stats_responses',
                    body=json.dumps(response_message),
                    properties=pika.BasicProperties(
                        delivery_mode=2,  
                    )
                )
                print(f"Respuesta enviada a la cola profile_visit_stats_responses: {json.dumps(response_message)}")
            finally:
                connection.close()
        else:
            print("No se proporcionó el ID del músico en el mensaje")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def start_consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='profile_visit_stats_requests', durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='profile_visit_stats_requests', on_message_callback=process_message)

    print('Esperando mensajes. Para salir presiona CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    with app.app_context():
        start_consumer()
