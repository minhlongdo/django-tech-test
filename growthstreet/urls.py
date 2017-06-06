from django.conf.urls import include, url
from django.contrib import admin
from loans.views import BorrowerRegistrationView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^loans/', include('loans.urls')),
    url(r'^accounts/register/$', BorrowerRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls'))
]
