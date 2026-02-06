from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_countries, name='all_countries'),
    path('<int:id>/', views.country_detail, name='country_detail'),
]
