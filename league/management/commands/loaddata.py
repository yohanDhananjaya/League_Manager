from django.core.management.base import BaseCommand, CommandError
from league.utils import add_player, add_team, add_match, add_round, tournament_registration, add_coach, add_user_types, \
    add_users
import json
from django.conf import settings

FILE_PATH = str(settings.BASE_DIR) + '/league/'


class Command(BaseCommand):
    help = "Populates the fake data into database"

    def handle(self, *args, **options):
        try:
            with open(FILE_PATH + '/data/_tournaments.json') as tours:
                tours_json = json.load(tours)
            for tour in tours_json:
                tournament_registration(t_name=tour['name'])
            print('Tournament Added')

            with open(FILE_PATH + '/data/teams.json') as teams:
                teams_json = json.load(teams)
            for team in teams_json:
                add_team(team_name=team['name'], score=team['score'], matches=team['matches'],
                         win=team['win'], loss=team['loss'], draw=team['draw'])
            print('Teams Added')

            with open(FILE_PATH + '/data/coaches.json') as coaches:
                coaches_json = json.load(coaches)
            for coach in coaches_json:
                add_coach(name=coach['name'], team_id=coach['team'], tournament_id=coach['tournament'])
            print('Coaches Added')

            with open(FILE_PATH + '/data/players.json') as players:
                players_json = json.load(players)
            for player in players_json:
                add_player(_name=player['name'], _score=player['score'], _matches=player['matches_played'],
                           avg_core=player['average_score'], _height=player['height_in_cm'], _team=player['team'])
            print('Players Added')

            with open(FILE_PATH + '/data/rounds.json') as rounds:
                rounds_json = json.load(rounds)
            for _round in rounds_json:
                add_round(tournament_name=_round['name'], teams_count=_round['teams_count'],
                          tournament_id=_round['tournament_id'])
            print('Rounds Added')

            with open(FILE_PATH + '/data/matches.json') as matches:
                matches_json = json.load(matches)
            for match in matches_json:
                add_match(winner_id=match['winner'], loser_id=match['loser'], win_score=match['winner_score'],
                          loser_score=match['loser_score'], round_id=match['round'], tournament_id=match['tournament'])
            print('Matches added')

            with open(FILE_PATH + '/data/user_types.json') as types:
                types_json = json.load(types)
            for _type in types_json:
                add_user_types(typename=_type['name'])
            print('User types added')

            with open(FILE_PATH + '/data/users.json') as users:
                users_json = json.load(users)
            for user in users_json:
                add_users(user_email=user['email'], user_type=user['type'])
            print('User types added')

            print('\nFake data loaded successfully!')

        except Exception as error:
            raise CommandError("Something went wrong\n", error)
