from django.db import models

class PlayerScore(models.Model):
    username = models.CharField(max_length=100)
    score = models.IntegerField()

    def __str__(self):
        return f'{self.username} - {self.score}'
