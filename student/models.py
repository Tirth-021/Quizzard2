from django.conf import settings
from django.db import models

from authentication.models import User
from questions.models import Quiz_settings

# Create your models here.
class LeaderBoard(models.Model):
    gamepin = models.ForeignKey(Quiz_settings, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def join(self, user):
        self.online.add(user)
        self.save()

    def __str__(self):
        return f'{self.user_id}'







