from django.db import models

class Player(models.Model):
    id_player = models.CharField(max_length=10, unique=True, verbose_name="ID hráče", blank=True, null=True)  # Přidané pole id_player
    last_name = models.CharField(max_length=100, verbose_name="Lastname")
    first_name = models.CharField(max_length=100, verbose_name="Firtname")
    birth_year = models.IntegerField(verbose_name="Birthyear")
    club = models.CharField(max_length=100, verbose_name="Club")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.id_player})"