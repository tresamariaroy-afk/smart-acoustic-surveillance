from django.urls import path
from . import views

urlpatterns = [
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('transcripts/', views.transcripts, name='transcripts'),
    path('toxic-words/', views.toxic_words, name='toxic_words'),
    path('reports/', views.reports, name='reports'),
    path('settings/', views.system_settings, name='system_settings'),
]