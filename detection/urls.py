from django.urls import path
from . import views

urlpatterns = [
    path('clips/', views.audio_clips, name='audio_clips'),
    path('live/', views.live_detection, name='live_detection'),
]