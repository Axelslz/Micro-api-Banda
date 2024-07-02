from flask import request, jsonify
from src.infrastructure.repositories.musician_repository import MusicianRepositoryImpl
from src.application.use_cases.musician_use_cases import RegisterMusicianUseCase

def register_musician():
    data = request.json
    repository = MusicianRepositoryImpl()
    use_case = RegisterMusicianUseCase(repository)
    musician = use_case.execute(data)
    return jsonify(musician.to_dict()), 201

