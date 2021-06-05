from rest_framework.decorators import api_view
from rest_framework.response import Response
from league.utils import tournament_progress, get_team, get_player, get_players_by_avg_percentile, user_login, \
    user_logout, get_user_info
from league.decorators import allowed_users


@api_view(["POST"])
@allowed_users(allowed_roles=[1])
def user_info(request):
    status, message, data = get_user_info()
    return Response({"status": status, "message": message, "data": data})


@api_view(["POST"])
def log_out(request):
    status, message = user_logout(request.data['email'])
    return Response({"status": status, "message": message})


@api_view(["POST"])
def log_in(request):
    status, message = user_login(request.data['email'])
    return Response({"status": status, "message": message})


@api_view(["POST"])
@allowed_users(allowed_roles=[1, 2])
def get_players_by_percentile(request):
    data = get_players_by_avg_percentile(request.data['team_id'], request.data['percentile'])
    return Response(data)


@api_view(["POST"])
@allowed_users(allowed_roles=[1, 2])
def get_player_details(request):
    data = get_player(request.data['player_id'])
    return Response(data)


@api_view(["POST"])
@allowed_users(allowed_roles=[1, 2])
def get_team_members(request):
    data = get_team(request.data['team_id'])
    return Response(data)


@api_view(["POST"])
@allowed_users(allowed_roles=[1, 2, 3])
def get_tournament_progress(request):
    data = tournament_progress()
    return Response(data)
