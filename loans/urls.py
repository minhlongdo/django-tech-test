from django.conf.urls import url
from .views import render_request_loan


urlpatterns = [
    url(r'request/', render_request_loan, name='request_loan')
]
