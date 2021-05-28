from django.db import models


class Team(models.Model):
    class LEAGUE(models.TextChoices):
        NATIONAL = 'National'
        AMERICAN = 'American'

    class DIVISION(models.TextChoices):
        EAST = 'East'
        CENTRAL = 'Central'
        WEST = 'West'

    name = models.CharField(max_length=50)
    league = models.CharField(max_length=10, choices=LEAGUE.choices, blank=True)
    division = models.CharField(max_length=10, choices=DIVISION.choices, blank=True)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    class W_OR_L(models.TextChoices):
        W = 'W'
        L = 'L'

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date = models.CharField(max_length=50, blank=True, null=True)
    opp = models.CharField(max_length=50, blank=True, null=True)
    team_win_prob = models.CharField(max_length=50, blank=True, null=True)
    w_or_l = models.CharField(max_length=10, choices=W_OR_L.choices, blank=True, null=True)
    team_runs = models.IntegerField(blank=True, null=True)
    opp_runs = models.IntegerField(blank=True, null=True)
    team_starter = models.CharField(max_length=100, blank=True, null=True)
    opp_starter = models.CharField(max_length=100, blank=True, null=True)
