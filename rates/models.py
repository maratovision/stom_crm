from django.db import models
from accounts.models import *


class Rate(models.Model):
    """This model is for rate of staff"""
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(StomProfile, on_delete=models.CASCADE)
    mark = models.PositiveIntegerField()
    comment = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.doctor} {self.mark}'
