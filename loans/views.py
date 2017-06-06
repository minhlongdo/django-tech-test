from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from registration.backends.simple.views import RegistrationView

from loans.forms import BorrowerRegistrationForm
from loans.models import Borrower

from django.conf import settings


class BorrowerRegistrationView(RegistrationView):

    form_class = BorrowerRegistrationForm

    def get_success_url(self, user=None):
        return '/accounts/login/'

    def register(self, form):
        new_user = super(BorrowerRegistrationView, self).register(form)

        user_borrower = Borrower()
        user_borrower.user = new_user
        user_borrower.number = form.cleaned_data['number']
        user_borrower.save()

        return user_borrower


@login_required(redirect_field_name=settings.LOGIN_URL)
def render_request_loan(request):
    return render(request, 'loans/request_loan.html')
