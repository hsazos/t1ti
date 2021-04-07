from django.urls import path
from .views import home, season_bb, season_bcs, episode_bb, episode_bcs, characters, buscar

urlpatterns = [
    path("", home, name="home"),
    path('bb/<int:season_id>/', season_bb, name="season_bb"),
    path('bcs/<int:season_id>/', season_bcs, name="season_bcs"),
    path('bb/<str:episode_name>/', episode_bb, name="episode_bb"),
    path('bcs/<str:episode_name>/', episode_bcs, name="episode_bcs"),
    path('characters/<str:character_name>/', characters, name="characters"),
    path('buscar/', buscar, name="buscar")
]