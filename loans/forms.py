from django.core.exceptions import ValidationError
from registration.forms import RegistrationFormUniqueEmail
from django import forms

from loans.models import Loan


class BorrowerRegistrationForm(RegistrationFormUniqueEmail):
    number = forms.CharField()


class LoanForm(forms.ModelForm):

    class Meta:
        model = Loan
        exclude = ('borrower', 'loan_id',)

    def clean_amount(self):
        amount = self.cleaned_data['amount'].amount

        if not (10000.00 <= amount <= 100000):
            raise ValidationError('Loan request has to be between 10000.00 GBP and 100000.00 GBP')

        return amount

    def clean_days(self):
        days = self.cleaned_data['days']
        if days <= 0:
            raise ValidationError('Number of days has to be greater than 0')

        return days
