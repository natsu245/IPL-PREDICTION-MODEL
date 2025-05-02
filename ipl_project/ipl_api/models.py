from django.db import models

# Model for Team
class Team(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Model for Player
class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    total_runs = models.IntegerField()  # Ensure this field is present
    total_wickets = models.IntegerField()




class Match(models.Model):
    team1 = models.ForeignKey(Team, related_name='team1', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2', on_delete=models.CASCADE)
    date = models.DateField()
    winner = models.ForeignKey(Team, on_delete=models.CASCADE)
    result = models.CharField(max_length=255)  # Make sure this field is present



