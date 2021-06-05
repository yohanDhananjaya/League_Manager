from django.urls import path
from . import views

urlpatterns = [
    path("tournament_progress", views.get_tournament_progress, name="tournament_progress"),
    path("get_team_details", views.get_team_members, name="get_team_details"),
    path("get_player_details", views.get_player_details, name="get_player_details"),
    path("get_players_by_percentile", views.get_players_by_percentile, name="get_players_by_percentile"),
    path("login", views.log_in, name="login"),
    path("logout", views.log_out, name="logout"),
    path("user_info", views.user_info, name="user_info"),
]
