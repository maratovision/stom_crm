from django.urls import path
from .views import *


urlpatterns = [
    path('stom/',StomProfileView.as_view(),name= 'staff'),
    path('signup/', SighUpView.as_view(), name= 'login'),
    path('clients/', UserProfileView.as_view(), name= 'clients'),
    path('stom/<int:stomprofile_id>/', StomProfileDetailView.as_view()),
    path('stom/<int:stomprofile_id>/<int:drtime_id>/', DrTimeDetailView.as_view())
]