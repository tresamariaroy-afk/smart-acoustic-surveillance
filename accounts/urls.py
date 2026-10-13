from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('authorities/', views.manage_authorities, name='manage_authorities'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
]