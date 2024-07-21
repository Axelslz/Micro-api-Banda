import sys
import os

# Agregar el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import json
from src.infrastructure.rabbitmq.rabbitmq_config import connect_rabbitmq
from src.infrastructure.repositories.musician_repository import MusicianRepositoryImpl
from src.infrastructure.database.mysql.connection import db
from flask import Flask

# Configura la aplicación Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/bandconnect'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

repository = MusicianRepositoryImpl()

def process_message(ch, method, properties, body):
    print("Mensaje recibido:", body)
    message = json.loads(body.decode('utf-8'))
    musician_id = int(message['musician_id'])
    
    with app.app_context():
        musician = repository.find_by_id(musician_id)
        if musician:
            print(f"Músico encontrado: {musician.to_dict()}")
        else:
            print(f"Músico con ID {musician_id} no encontrado")

def start_consumer():
    connection, channel = connect_rabbitmq()
    try:
        queue = 'musician_requests'
        channel.queue_declare(queue=queue, durable=True)

        channel.basic_consume(queue=queue, on_message_callback=process_message, auto_ack=True)
        print('Esperando mensajes. Para salir presiona CTRL+C')
        channel.start_consuming()
    except KeyboardInterrupt:
        print("Cerrando conexión...")
        connection.close()

if __name__ == '__main__':
    start_consumer()


