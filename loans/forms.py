from registration.forms import RegistrationFormUniqueEmail
from django import forms

from loans.models import Loan


class BorrowerRegistrationForm(RegistrationFormUniqueEmail):
    number = forms.CharField()


class LoanForm(forms.ModelForm):

    class Meta:
        model = Loan
        exclude = ('borrower', 'loan_id',)
