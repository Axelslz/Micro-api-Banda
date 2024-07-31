from flask import request, jsonify
from src.domain.entities.musician import Musician
from src.application.use_cases.musician_use_cases import RegisterMusicianUseCase, FindMusicianByIdUseCase
from src.application.use_cases.login_use_case import LoginMusicianUseCase
from src.application.use_cases.profile_visit_use_case import ProfileVisitStatsUseCase, RecordProfileVisitUseCase, GetProfileVisitStatsUseCase
from src.infrastructure.repositories.musician_repository import MusicianRepositoryImpl
from src.infrastructure.rabbitmq.rabbitmq_helper import receive_from_rabbitmq, send_to_rabbitmq

repository = MusicianRepositoryImpl()
profile_visit_stats_use_case = ProfileVisitStatsUseCase(repository)

def register_musician():
    data = request.get_json()
    use_case = RegisterMusicianUseCase(repository)
    try:
        musician_dict = use_case.execute(data)  # Asegúrate de obtener un diccionario
        welcome_message = f"Bienvenido a BandConnect, {musician_dict['name']}!"
        return jsonify({"message": welcome_message}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
def find_musician_by_id(musician_id):
    use_case = FindMusicianByIdUseCase(repository)
    response = use_case.execute(musician_id)
    
    # Registrar visita al perfil
    record_visit_use_case = RecordProfileVisitUseCase(repository)
    record_visit_use_case.execute(musician_id)
    
    send_to_rabbitmq('musician_requests', {'musician_id': musician_id})
    
    return jsonify(response)

def login_musician():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400
    email = data.get('email')
    password = data.get('password')
    use_case = LoginMusicianUseCase(repository)
    response = use_case.execute(email, password)
    
    send_to_rabbitmq('login_requests', {'email': email, 'password': password})
    
    return jsonify(response)


def get_profile_visit_stats(musician_id):
    send_to_rabbitmq('profile_visit_stats_requests', {'musician_id': musician_id})
    stats = receive_from_rabbitmq('profile_visit_stats_responses')
    
    if stats is None:
        return jsonify({"error": "No se recibieron datos de visitas"}), 500
    
    return jsonify(stats)