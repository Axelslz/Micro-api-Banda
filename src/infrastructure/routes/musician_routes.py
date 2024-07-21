from flask import Blueprint
from src.infrastructure.controllers.musician_controller import register_musician, find_musician_by_id

musician_routes = Blueprint('musician_routes', __name__)

musician_routes.route('/register', methods=['POST'])(register_musician)
musician_routes.route('/find', methods=['GET'])(find_musician_by_id)
