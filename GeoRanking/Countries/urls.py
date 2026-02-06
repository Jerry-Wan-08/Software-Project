from django.urls import path
from . import views

urlpatterns = [
    path('Countries/', views.Countries, name='Countries'),
]