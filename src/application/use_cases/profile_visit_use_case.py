import os
from src.infrastructure.repositories.musician_repository import MusicianRepositoryImpl
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta


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
        plt.plot(weekly_visits, marker='o', label='Visitas reales')
        plt.title('Visitas al perfil por semana')
        plt.xlabel('Semana')
        plt.ylabel('Número de visitas')
        plt.grid(True)

        # Predicción simple usando promedio móvil
        if len(weekly_visits) >= 3:
            prediction = weekly_visits[-3:].mean()  # Promedio de las últimas 3 semanas
        else:
            prediction = weekly_visits.mean()  # Promedio de todas las semanas disponibles si hay menos de 3 semanas

        next_week = weekly_visits.index[-1] + timedelta(weeks=1)
        plt.axvline(x=next_week, color='r', linestyle='--', label='Semana predicha')
        plt.scatter([next_week], [prediction], color='r')
        plt.legend()

        # Verificar y crear la carpeta si no existe
        graphics_folder = 'graphics'
        if not os.path.exists(graphics_folder):
            os.makedirs(graphics_folder)

        # Guardar la gráfica en la carpeta
        graph_path = os.path.join(graphics_folder, 'profile_visit_trends.png')
        plt.savefig(graph_path)

        # Generar recomendaciones
        if prediction < weekly_visits.mean():
            recommendation = "Se recomienda subir publicaciones para aumentar las visitas."
        else:
            recommendation = "¡Buen trabajo! Sigue subiendo contenido regularmente para mantener las visitas."

        # Convertir claves a str
        weekly_visits_str_keys = {str(k): v for k, v in weekly_visits.items()}

        # Retornar estadísticas y ruta de la imagen
        return {
            'weekly_visits': weekly_visits_str_keys,
            'predicted_visits': prediction,
            'graph_path': graph_path,
            'recommendation': recommendation
        }
    
class ProfileVisitStatsUseCase:
    def __init__(self, repository: MusicianRepositoryImpl):
        self.repository = repository

    def execute(self, musician_id: int):
        visits = self.repository.get_profile_visits(musician_id)
        visit_counts = {date: visits.count(date) for date in visits}
        return visit_counts

