from django.core.exceptions import ValidationError
from registration.forms import RegistrationFormUniqueEmail
from django import forms

from loans.models import Loan, Business, BUSINESS_SECTOR, Borrower


class BorrowerRegistrationForm(RegistrationFormUniqueEmail):
    number = forms.CharField()


class LoanForm(forms.ModelForm):

    class Meta:
        model = Loan
        exclude = ('borrower', 'loan_id',)

    def __init__(self, user, *args, **kwargs):
        super(LoanForm, self).__init__(*args, **kwargs)

        owner = Borrower.objects.get(user=user)

        user_businesses = Business.objects.filter(owner=owner)

        business_list = []

        for businesses in user_businesses:
            business_list.append((businesses.id, businesses.name))

        self.fields['business'] = forms.CharField(widget=forms.Select(choices=business_list))

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


class BusinessForm(forms.ModelForm):

    class Meta:
        model = Business
        exclude = ('owner',)
        widgets = {
            'business_sector': forms.Select(choices=BUSINESS_SECTOR)
        }
