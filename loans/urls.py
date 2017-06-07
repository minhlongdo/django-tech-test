from django.conf.urls import url
from .views import request_loan, render_request_loan, render_add_business

urlpatterns = [
    url(r'options/$', render_request_loan, name='request_options'),
    url(r'request/$', request_loan, name='request_loan'),
    url(r'business/register/$', render_add_business, name='register_business')
]
