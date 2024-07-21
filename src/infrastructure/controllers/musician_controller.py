from flask import request, jsonify
from src.application.use_cases.musician_use_cases import RegisterMusicianUseCase, FindMusicianByIdUseCase
from src.infrastructure.repositories.musician_repository import MusicianRepositoryImpl

repository = MusicianRepositoryImpl()

def register_musician():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    use_case = RegisterMusicianUseCase(repository)
    message = use_case.execute(data)
    
    return jsonify({"message": message})

def find_musician_by_id():
    musician_id = request.args.get('id')
    response = FindMusicianByIdUseCase.execute(musician_id)
    return jsonify(response)