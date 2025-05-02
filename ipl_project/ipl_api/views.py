from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Team, Player, Match
from .serializers import TeamSerializer, PlayerSerializer, MatchSerializer

# View for displaying all teams
class TeamListView(APIView):
    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)


# View for displaying all players
class PlayerListView(APIView):
    def get(self, request):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)


# View for displaying all matches
class MatchListView(APIView):
    def get(self, request):
        matches = Match.objects.all()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)


