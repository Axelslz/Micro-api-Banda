from flask import Flask
from src.infrastructure.controllers.musician_controller import register_musician

def configure_routes(app: Flask):
    app.add_url_rule('/musicians/register', 'register_musician', register_musician, methods=['POST'])
