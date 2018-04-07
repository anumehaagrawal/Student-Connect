from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
from datetime import datetime

class College(models.Model):
    college_id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    reviews = models.CharField(max_length=1000)
    fees = models.CharField(max_length=255)
    exam = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    specialisation = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    ethnicity = models.CharField(max_length=255)
    ratings = models.IntegerField()

    @property
    def college_id(self):
        return self.id

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_counsellor = models.BooleanField(default=False)

class Counsellor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    last_login = models.DateTimeField(default=datetime.now)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    sat_score = models.CharField(max_length=255)
    act_score = models.CharField(max_length=255)
    gpa = models.CharField(max_length=255)
    ethnicity = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

class Passout(models.Model):
	name = models.CharField(max_length=255)
	counsellor_username = models.CharField(max_length=255)
