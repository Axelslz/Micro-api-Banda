from src.infrastructure.repositories.musician_repository import MusicianRepositoryImpl

class RecordProfileVisitUseCase:
    def __init__(self, repository: MusicianRepositoryImpl):
        self.repository = repository

    def execute(self, musician_id: int):
        print(f"Registrando visita al perfil para el músico con ID {musician_id}")
        self.repository.record_profile_visit(musician_id)

class GetProfileVisitStatsUseCase:
    def __init__(self, repository: MusicianRepositoryImpl):
        self.repository = repository

    def execute(self, musician_id: int) -> dict:
        visits = self.repository.get_profile_visits(musician_id)
        return self._analyze_visits(visits)

    def _analyze_visits(self, visits):
        # Aquí puedes implementar la lógica de análisis y predicción.
        # Por ejemplo, contar visitas por semana y generar estadísticas.
        import matplotlib.pyplot as plt
        import pandas as pd
        from datetime import datetime, timedelta

        # Convertir las visitas a un DataFrame
        df = pd.DataFrame(visits, columns=['timestamp'])
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df.set_index('timestamp', inplace=True)

        # Resamplear por semana
        weekly_visits = df.resample('W').size()

        # Generar gráfica
        plt.figure(figsize=(10, 5))
        plt.plot(weekly_visits, marker='o')
        plt.title('Visitas al perfil por semana')
        plt.xlabel('Semana')
        plt.ylabel('Número de visitas')
        plt.grid(True)
        plt.savefig('profile_visit_trends.png')

        # Retornar estadísticas y ruta de la imagen
        return {
            'weekly_visits': weekly_visits.to_dict(),
            'graph_path': 'profile_visit_trends.png'
        }

class ProfileVisitStatsUseCase:
    def __init__(self, repository: MusicianRepositoryImpl):
        self.repository = repository

    def execute(self, musician_id: int):
        visits = self.repository.get_profile_visits(musician_id)
        visit_counts = {date: visits.count(date) for date in visits}
        return visit_counts
