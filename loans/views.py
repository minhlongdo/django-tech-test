from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.views import View
from registration.backends.simple.views import RegistrationView
from rest_framework.decorators import api_view

from loans.forms import BorrowerRegistrationForm, LoanForm, BusinessForm
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


@api_view(['GET', 'POST'])
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


@api_view(['GET'])
@login_required(redirect_field_name=settings.LOGIN_URL)
def render_request_loan(request):
    return render(request, 'loans/loan_options.html')


@api_view(['GET', 'POST'])
@login_required(redirect_field_name=settings.LOGIN_URL)
def render_add_business(request):
    if request.method == 'GET':
        form = BusinessForm()
        return render(request, 'loans/register_business.html', {'form': form})
    elif request.method == 'POST':
        form = BusinessForm(request.POST)

        if form.is_valid():
            new_business = form.save(commit=False)
            new_business.owner = Borrower.objects.get(user=request.user)
            new_business.save()

            return HttpResponseRedirect('loans/options/')
        else:
            form = BusinessForm()
            return render(request, 'loans/register_business.html', {'form': form})
