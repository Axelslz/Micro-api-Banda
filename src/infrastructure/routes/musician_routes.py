from flask import Blueprint
from src.infrastructure.controllers.musician_controller import register_musician, find_musician_by_id, login_musician, get_profile_visit_stats, get_profile_visit_stats_and_graph

musician_routes = Blueprint('musician_routes', __name__)

musician_routes.route('/register', methods=['POST'])(register_musician)
musician_routes.route('/<string:musician_id>', methods=['GET'])(find_musician_by_id)
musician_routes.route('/login', methods=['POST'])(login_musician)
musician_routes.route('/<string:musician_id>/stats', methods=['GET'])(get_profile_visit_stats)
musician_routes.route('/<string:musician_id>/stats_and_graph', methods=['GET'])(get_profile_visit_stats_and_graph)