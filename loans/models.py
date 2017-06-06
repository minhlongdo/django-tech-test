from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Borrower(models.Model):
    number = PhoneNumberField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
