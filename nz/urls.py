from nz.views import *
from django.urls import path

app_name='anything'
urlpatterns=[
    path('philips/',philips,name='philips'),
    path('conway/',conway,name='conway'),
]