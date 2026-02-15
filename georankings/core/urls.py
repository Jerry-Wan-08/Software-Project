from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('rate/', views.rate_country, name='rate'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Blog URLs
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/create/', views.blog_create, name='blog_create'),
    path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('blog/<int:post_id>/edit/', views.blog_edit, name='blog_edit'),
    path('blog/<int:post_id>/delete/', views.blog_delete, name='blog_delete'),
]