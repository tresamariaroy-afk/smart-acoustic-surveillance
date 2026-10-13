from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.authority_dashboard, name='authority_dashboard'),
    path('alerts/', views.alerts, name='alerts'),
    path('alerts/<int:pk>/', views.alert_detail, name='alert_detail'),
    path('history/', views.history, name='history'),
]