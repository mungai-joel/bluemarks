from django.urls import path
from . import (
   views,
   api_views
)



urlpatterns = [
    path('',views.home, name='home'),
]
