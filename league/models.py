from django.db import models
from django.utils import timezone


class Tournament(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = True
        db_table = 'tournament'


class Player(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    score = models.IntegerField(null=True)
    matches_played = models.IntegerField(null=True)
    average_score = models.FloatField(null=True)
    height_in_cm = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = True
        db_table = 'player'


class Coach(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = True
        db_table = 'coach'


class Team(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    score = models.FloatField(null=True)
    matches = models.IntegerField(null=True)
    win = models.IntegerField(null=True)
    loss = models.IntegerField(null=True)
    draw = models.IntegerField(null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = True
        db_table = 'team'


class TeamPlayer(models.Model):
    id = models.BigAutoField(primary_key=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = True
        db_table = 'team_player'


class TournamentTeam(models.Model):
    id = models.BigAutoField(primary_key=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    score = models.FloatField(null=True, default=0)
    matches = models.IntegerField(null=True, default=0)
    win = models.IntegerField(null=True, default=0)
    loss = models.IntegerField(null=True, default=0)
    draw = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = True
        db_table = 'tournament_team'


class TournamentRound(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    teams_count = models.IntegerField()
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = True
        db_table = 'tournament_round'


class Match(models.Model):
    id = models.BigAutoField(primary_key=True)
    winner = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='winner')
    loser = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='loser')
    winner_score = models.IntegerField()
    loser_score = models.IntegerField()
    round = models.ForeignKey(TournamentRound, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = True
        db_table = 'match'


class UserType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = True
        db_table = 'user_type'


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(max_length=255)
    type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    log_count = models.IntegerField(default=0, null=True)
    log_time_seconds = models.IntegerField(default=0, null=True)
    is_online = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = True
        db_table = 'user'
