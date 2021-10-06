from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    tag = models.CharField(max_length=100)


class Appointment(models.Model):
    preferred_date = models.DateField()
    doctor_name = models.CharField(max_length=150)
    patient_name = models.CharField(max_length=150)
    phone_no = models.CharField(max_length=15)