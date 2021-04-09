from django.db import models
from accounts.models import *
from schedule.models import *


class Order(models.Model):
    """This model for creating order to visit"""
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(StomProfile, on_delete=models.CASCADE)
    dr_time = models.ForeignKey(DrTime, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    reason = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.client} {self.reason}'
