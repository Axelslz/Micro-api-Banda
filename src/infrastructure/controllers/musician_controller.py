from flask import request, jsonify
from src.application.use_cases.musician_use_cases import RegisterMusicianUseCase, FindMusicianByIdUseCase
from src.application.use_cases.login_use_case import LoginMusicianUseCase
from src.infrastructure.repositories.musician_repository import MusicianRepositoryImpl
from src.infrastructure.rabbitmq.rabbitmq_helper import send_to_rabbitmq

repository = MusicianRepositoryImpl()

def register_musician():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400
    use_case = RegisterMusicianUseCase(repository)
    message = use_case.execute(data)
    
    # Enviar mensaje a RabbitMQ
    send_to_rabbitmq('musician_created', {'musician': message})
    
    return jsonify({"message": message}), 201

def find_musician_by_id(musician_id):
    use_case = FindMusicianByIdUseCase(repository)
    response = use_case.execute(musician_id)
    
    # Enviar mensaje a RabbitMQ
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
    
    # Enviar mensaje a RabbitMQ
    send_to_rabbitmq('login_requests', {'email': email, 'password': password})
    
    return jsonify(response)
