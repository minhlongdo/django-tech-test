from registration.forms import RegistrationFormUniqueEmail
from django import forms


class BorrowerRegistrationForm(RegistrationFormUniqueEmail):
    number = forms.CharField()
