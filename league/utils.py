from league.models import *
from django.utils import timezone
import datetime


def tournament_registration(t_name):
    tournament = Tournament(name=t_name)
    tournament.save()
    return tournament


def get_tournaments():
    data = Tournament.objects.all()
    return data


def add_player(_name, _score, _matches, avg_core, _height, _team):
    player = Player(name=_name,
                    score=_score,
                    matches_played=_matches,
                    average_score=avg_core,
                    height_in_cm=_height)
    player.save()
    team = Team.objects.get(id=_team)
    add_team_player(player, team)
    return player


def add_team_player(player, team):
    team_player = TeamPlayer(player=player,
                             team=team)
    team_player.save()


def add_team(team_name, score, matches, win, loss, draw):
    team = Team(name=team_name,
                score=score,
                matches=matches,
                win=win,
                loss=loss,
                draw=draw)
    team.save()
    return team


def add_coach(name, team_id, tournament_id):
    coach = Coach(name=name)
    coach.save()
    add_tournament_team(tournament_id, team_id, coach)
    return coach


def add_tournament_team(tournament_id, team_id, coach):
    tournament = Tournament.objects.get(id=tournament_id)
    team = Team.objects.get(id=team_id)

    tournament_team = TournamentTeam(tournament=tournament,
                                     team=team,
                                     coach=coach)
    tournament_team.save()
    return tournament_team


def add_round(tournament_name, teams_count, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    t_round = TournamentRound(name=tournament_name,
                              teams_count=teams_count,
                              tournament=tournament)
    t_round.save()
    return t_round


def add_match(winner_id, loser_id, win_score, loser_score, round_id, tournament_id):
    winner = Team.objects.get(id=winner_id)
    loser = Team.objects.get(id=loser_id)
    t_round = TournamentRound.objects.get(id=round_id)
    tournament = Tournament.objects.get(id=tournament_id)

    match = Match(winner=winner,
                  loser=loser,
                  winner_score=win_score,
                  loser_score=loser_score,
                  round=t_round,
                  tournament=tournament)

    winner_team = TournamentTeam.objects.values_list('score', 'matches', 'win', 'loss', 'draw').get(team=winner)
    TournamentTeam.objects.filter(team=winner).update(score=int(winner_team[0]) + win_score,
                                                      matches=int(winner_team[1]) + 1,
                                                      win=int(winner_team[2]) + 1)

    loser_team = TournamentTeam.objects.values_list('score', 'matches', 'win', 'loss', 'draw').get(team=loser)
    TournamentTeam.objects.filter(team=loser).update(score=int(loser_team[0]) + loser_score,
                                                     matches=int(loser_team[1]) + 1,
                                                     loss=int(loser_team[3]) + 1)

    match.save()
    return match


def add_user_types(typename):
    user_type = UserType(name=typename)
    user_type.save()


def add_users(user_email, user_type):
    usertype = UserType.objects.get(id=user_type)
    user = User(email=user_email, type=usertype)
    user.save()


def tournament_progress():
    print('tournament_progress')
    teams = TournamentTeam.objects.order_by('-score')

    qualifier_list = []
    quarter_final_list = []
    semi_final_list = []
    final_list = []
    count = 1
    for team in teams:
        if team.matches == 1:
            qualifier_list.append({'team name': team.team.name, 'coach name': team.coach.name,
                                   'matches': team.matches, 'win': team.win, 'loss': team.loss,
                                   'draw': team.draw, 'standing': count})
        elif team.matches == 2:
            quarter_final_list.append({'team name': team.team.name, 'coach name': team.coach.name,
                                       'matches': team.matches, 'win': team.win, 'loss': team.loss,
                                       'draw': team.draw, 'standing': count})
        elif team.matches == 3:
            semi_final_list.append({'team name': team.team.name, 'coach name': team.coach.name,
                                    'matches': team.matches, 'win': team.win, 'loss': team.loss,
                                    'draw': team.draw, 'standing': count})
        if team.matches == 4:
            final_list.append({'team name': team.team.name, 'coach name': team.coach.name,
                               'matches': team.matches, 'win': team.win, 'loss': team.loss,
                               'draw': team.draw, 'standing': count})
        count += 1

    response = {'qualifier round': qualifier_list, 'quarter final round': quarter_final_list,
                'semi final round': semi_final_list, 'final round': final_list}
    return response


def get_team(team_id):

    team = Team.objects.values_list('name', 'score', 'matches').get(id=team_id)
    avg_score = round((int(team[1]) / int(team[2])), 2)

    players = TeamPlayer.objects.filter(team=team_id)
    players_list = []
    for team_player in players:
        players_list.append(team_player.player.name)

    team_dict = {'team name': team[0], 'average score': avg_score, 'players': players_list}

    return team_dict


def get_player(player_id):
    player = Player.objects.get(id=player_id)
    response = {'player name': player.name, 'height in cm': player.height_in_cm,
                'matches played': player.matches_played,
                'average score': player.average_score}
    return response


def get_players_by_avg_percentile(team_id, percentile):
    players_list = []
    players = TeamPlayer.objects.filter(team=team_id).order_by('player__average_score')
    index = round(int(percentile)/100 * len(players))

    for team_player in players[index:]:
        player = team_player.player
        players_list.append(player.name)

    response = {f'{percentile} percentile players': players_list}
    return response


def user_login(user_email):
    if User.objects.filter(email=user_email).exists():
        user_data = User.objects.values_list('is_online', 'log_count').get(email=user_email)
        if user_data[0] == 1:
            return True, "User Already Logged in"
        else:
            User.objects.filter(email=user_email).update(log_count=int(user_data[1])+1, last_login=timezone.now(),
                                                         is_online=1)
            return True, "Login Successful"
    else:
        return False, "Unauthorized User"


def user_logout(user_email):
    if User.objects.filter(email=user_email).exists():
        user_data = User.objects.values_list('is_online', 'log_time_seconds', 'last_login').get(email=user_email)
        if user_data[0] == 1:
            logged_time = round((timezone.now() - user_data[2]).total_seconds())
            total_logged_time = user_data[1] + logged_time
            User.objects.filter(email=user_email).update(log_time_seconds=total_logged_time, is_online=0)
            return True, "Logout Successful"
        else:
            return True, "User is not logged in"
    else:
        return False, "Unauthorized User"


def get_user_info():
    user_details = []
    online_users = []
    users = User.objects.all()
    for user in users:
        user_details.append({'user_id': user.id, 'user_email': user.email, 'number_of_login_times': user.log_count,
                             'total_time(second)_spent_on_site': user.log_time_seconds, 'is_online': user.is_online})
        if user.is_online == 1:
            online_users.append(user.email)

    response = {'online_users': online_users, 'user_details': user_details}
    return True, "Data Retrieve Success", response
