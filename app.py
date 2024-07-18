from flask import Flask
from src.infrastructure.routes.routes import configure_routes
from src.infrastructure.database.mysql.connection import init_db
from src.infrastructure.rabbitmq.rabbitmq_config import connect_rabbitmq
from src.infrastructure.rabbitmq.musician_subscriber import start_musician_subscriber

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
configure_routes(app)
init_db(app)

def start_app():
    connection, channel = connect_rabbitmq()
    start_musician_subscriber()

    app.run(debug=True)

if __name__ == '__main__':
    start_app()

