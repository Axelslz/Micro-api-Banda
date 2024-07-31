from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
db = SQLAlchemy()

def create_database_if_not_exists():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
    )
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS bandconnect")
    cursor.close()
    connection.close()

def init_db(app):
    create_database_if_not_exists()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/bandconnect'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
