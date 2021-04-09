from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    """This model is for create client account"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    date_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=(
        ('male', 'male'),
        ('female', 'female')
    ))

    def __str__(self):
        return self.full_name


class StomProfile(models.Model):
    """This model is for create staff account"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    photo = models.ImageField(blank=True, null=True)
    position = models.CharField(max_length=50)
    bio = models.CharField(max_length=200)
    exp = models.CharField(max_length=200)
    education = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class MedicalBook(models.Model):
    """This model for saving medial history of client"""
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(StomProfile, on_delete=models.CASCADE)
    reason = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.client} {self.reason}'
