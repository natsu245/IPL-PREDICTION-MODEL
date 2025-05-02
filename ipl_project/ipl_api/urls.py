from django.urls import path
from . import views

urlpatterns = [
    path('teams/', views.TeamListView.as_view(), name='teams'),
    path('players/', views.PlayerListView.as_view(), name='players'),
    path('matches/', views.MatchListView.as_view(), name='matches'),
]


