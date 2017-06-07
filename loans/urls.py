from django.conf.urls import url
from .views import request_loan


urlpatterns = [
    url(r'request/', request_loan, name='request_loan')
]
