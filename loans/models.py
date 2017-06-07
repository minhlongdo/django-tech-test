from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from djmoney.models.fields import MoneyField
from phonenumber_field.modelfields import PhoneNumberField


class Borrower(models.Model):
    number = PhoneNumberField(unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


BUSINESS_SECTOR = [
    ('retail', 'Retail'),
    ('professional_services', 'Professional Services'),
    ('food_drinks', 'Food & Drinks'),
    ('entertainment', 'Entertainment')
]


class Business(models.Model):
    owner = models.ForeignKey(Borrower)
    name = models.CharField(max_length=255, blank=False)
    address = models.CharField(max_length=255)
    registered_company = models.CharField(max_length=8, blank=False, unique=True)
    business_sector = models.TextField(choices=BUSINESS_SECTOR, blank=True)


class Loan(models.Model):
    loan_id = models.IntegerField(primary_key=True, auto_created=True)
    borrower = models.ForeignKey(Borrower, on_delete=models.PROTECT)
    amount = MoneyField(max_digits=8, decimal_places=2,
                        max_length=6, default_currency='GBP')
    days = models.IntegerField(default=0)
    reason = models.TextField(blank=False)
    business = models.ForeignKey(Business, default=None)

    def clean(self):
        if self.days is None or self.days <= 0:
            raise ValidationError({'days': 'Repayment day cannot be 0'})

        if not (10000.00 <= float(self.amount) <= 100000.00):
            raise ValidationError({'amount': 'Loan request has to be between 10000.00 GBP and 100000.00 GBP'})

        if not self.reason:
            raise ValidationError({'reason': 'Loan reason cannot be empty'})

        if self.business is None:
            raise ValidationError({'business': 'Loan needs to be registered to a business'})
