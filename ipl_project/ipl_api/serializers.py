from rest_framework import serializers
from .models import Team, Player, Match


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'city']


class PlayerSerializer(serializers.ModelSerializer):
    team = TeamSerializer()  # Nested team info

    class Meta:
        model = Player
        fields = ['id', 'name', 'team', 'role', 'total_runs', 'total_wickets']


class MatchSerializer(serializers.ModelSerializer):
    team1 = TeamSerializer()
    team2 = TeamSerializer()
    winner = TeamSerializer()

    class Meta:
        model = Match
        fields = ['id', 'team1', 'team2', 'date', 'winner', 'result']
