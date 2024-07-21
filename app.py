from flask import Flask
from src.infrastructure.routes.musician_routes import musician_routes
from src.infrastructure.database.mysql.connection import init_db

app = Flask(__name__)
app.register_blueprint(musician_routes, url_prefix='/')
init_db(app)

if __name__ == '__main__':
    app.run(debug=True, port=5000)



