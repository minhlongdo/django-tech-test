from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User

from loans.models import Borrower, Business, Loan

admin.site.unregister(User)
admin.site.register(Borrower)
admin.site.register(Business)
admin.site.register(Loan)