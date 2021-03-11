from django.db import models


class FootballTeam(models.Model):
    name = models.CharField(max_length=50, verbose_name="Takım Adı")

    squad = []
    teamPower = 0
    squadValue = 0
    numOfTeamMembers = 0



    def __str__(self):
        myStr = self.name
        return myStr
