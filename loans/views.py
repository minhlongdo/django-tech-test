from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.views import View
from registration.backends.simple.views import RegistrationView

from loans.forms import BorrowerRegistrationForm, LoanForm
from loans.models import Borrower, Loan

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
def request_loan(request):
    if request.method == 'GET':
        form = LoanForm()
        return render(request, 'loans/request_loan.html',
                      {'form': form})
    elif request.method == 'POST':
        form = LoanForm(request.POST)

        if form.is_valid():
            loan_request = form.save(commit=False)
            loan_request.borrower = Borrower.objects.get(user=request.user)
            loan_request.save()

            return HttpResponseRedirect('loans/request/')
        else:
            print("error")
            form = LoanForm()
            return render(request, 'loans/request_loan.html', {'form': form})
    else:
        form = LoanForm
        return render(request, 'loans/request_loan.html', {'form': form})
