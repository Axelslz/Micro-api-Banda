from flask import Flask
from src.infrastructure.routes.routes import configure_routes
from src.database.mysql.connection import init_db

app = Flask(__name__)
configure_routes(app)
init_db(app)

if __name__ == '__main__':
    app.run(debug=True)
