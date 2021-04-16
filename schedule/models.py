from django.db import models
from accounts.models import *


class Day(models.Model):
    """This model is for create days of the week"""
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    """This model is for create schedule of doctor"""
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    time = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.day} {self.time}'


class DrTime(models.Model):
    """This model is for create doctor's page"""
    doctor = models.ForeignKey(StomProfile, on_delete=models.CASCADE, related_name='drtime')
    schedule = models.OneToOneField(Schedule, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=(
        ('empty', 'empty'),
        ('busy', 'busy')
    ))

    def __str__(self):
        return f'{self.doctor} {self.schedule} {self.status}'
