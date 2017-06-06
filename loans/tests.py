from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase
from moneyed import Money, GBP

from .models import Loan, Borrower


class LoanModelTest(TestCase):

    def test_valid_loan_model(self):
        user = User.objects.create_user('test', 'test@domain.com', 'test_password')
        loan_reason = 'loan_reason'
        amount = Money(50000, GBP)
        borrower = Borrower(number='+445381269825', user=user)

        loan = Loan(borrower=borrower, reason=loan_reason, amount=amount, days=1)

        loan.clean()

    def test_invalid_money_value(self):
        user = User.objects.create_user('test', 'test@domain.com', 'test_password')
        loan_reason = 'loan_reason'
        amount = Money(5000, GBP)
        borrower = Borrower(number='+445381269825', user=user)

        loan = Loan(borrower=borrower, reason=loan_reason, amount=amount, days=1)

        with self.assertRaises(ValidationError):
            loan.clean()

    def test_empty_loan_reason(self):
        user = User.objects.create_user('test', 'test@domain.com', 'test_password')
        loan_reason = ''
        amount = Money(50000, GBP)
        borrower = Borrower(number='+445381269825', user=user)

        loan = Loan(borrower=borrower, reason=loan_reason, amount=amount, days=1)

        with self.assertRaises(ValidationError):
            loan.clean()

    def test_invalid_day_count(self):
        user = User.objects.create_user('test', 'test@domain.com', 'test_password')
        loan_reason = ''
        amount = Money(50000, GBP)
        borrower = Borrower(number='+445381269825', user=user)

        loan = Loan(borrower=borrower, reason=loan_reason, amount=amount, days=0)

        with self.assertRaises(ValidationError):
            loan.clean()
