from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from footballteam.models import FootballTeam


class Footballer(models.Model):
    name = models.CharField(max_length=50, verbose_name="Oyuncu Adı")
    # teamName = models.CharField(max_length=50, verbose_name="Takım Adı", null=True)
    age = models.IntegerField(verbose_name="Oyuncu Yaşı",
                              validators=[MinValueValidator(15), MaxValueValidator(50)], default=17)
    overall = models.IntegerField(verbose_name="Oyuncunun Gücü(40-99)",
                                  validators=[MinValueValidator(40), MaxValueValidator(99)], default=70)

    class Position(models.TextChoices):
        forvet = "fv",
        ortaSaha = "os",
        defans = "def",
        kaleci = "kl"

    team = models.ManyToManyField(FootballTeam, verbose_name="Takım", blank=True)

    position = models.CharField(choices=Position.choices, default=Position.forvet, max_length=10)
    salary = models.DecimalField(verbose_name="Oyuncunun Maaşı",
                                 validators=[MinValueValidator(0)], decimal_places=2, max_digits=10)
    marketValue = models.DecimalField(verbose_name="Oyuncunun değeri",
                                      validators=[MinValueValidator(0)], decimal_places=2, max_digits=10)

    def __str__(self):
        myStr = self.name
        return myStr
