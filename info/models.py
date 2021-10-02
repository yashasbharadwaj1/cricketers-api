from django.db import models


# Create your models here.
class gameformat(models.Model):
    format = models.CharField(max_length=150, blank=False, default='')

    def __str__(self):
        return self.format


class Team(models.Model):
    name = models.CharField(max_length=250)
    game_format= models.ForeignKey(gameformat,
                                       related_name='formats',
                                       on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Player(models.Model):
    batsman = 'batsman'
    bowler = 'bowler'
    all_rounder = 'allrounder'
    CHOICES = (
        (batsman, 'batsman'),
        (bowler, 'bowler'),
        (all_rounder, 'allrounder')
    )
    name = models.CharField(max_length=150, blank=False, default='')
    role_in_team = models.CharField(
        max_length=100,
        choices=CHOICES,
        default=all_rounder,
    )
    matches_played_so_far = models.IntegerField()
    year_of_entry_into_team = models.DateTimeField()

    class Meta:
        ordering = ('matches_played_so_far',)

    def __str__(self):
        return self.name


class tournament(models.Model):
    tournament_name = models.CharField(max_length=150, blank=False, default='')
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE)
    no_of_titles = models.IntegerField()

    class Meta:
        ordering = ('-no_of_titles',)

    def __str__(self):
        return self.tournament_name
