from django.urls import path
from .views import *


urlpatterns = [
    path('rates/', RateView.as_view(), name= 'rates')
]