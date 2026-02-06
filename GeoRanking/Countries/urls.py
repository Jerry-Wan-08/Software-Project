from django.urls import path
from . import views

urlpatterns = [
    path('Countries/', views.all_countries, name='Countries'),
]