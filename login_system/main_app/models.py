# authentication/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('normal', 'Normal User'),
        ('premium', 'Premium User'),
        ('admin', 'Admin User'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='normal')
    phone_number = models.CharField(max_length=20, blank=True)
