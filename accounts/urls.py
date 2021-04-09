from django.urls import path
from .views import *


urlpatterns = [
    path('',StomProfileView.as_view(),name= 'staff')
]