from django.urls import path
from .views import *


urlpatterns = [
    path('drtimes/', DrTimeView.as_view(), name= 'drtimes')
]