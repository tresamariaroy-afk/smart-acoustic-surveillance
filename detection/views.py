from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import AudioClip


@login_required
def audio_clips(request):
    clips = AudioClip.objects.all().order_by('-uploaded_at')
    return render(request, 'detection/audio_clips.html', {'clips': clips})


@login_required
def live_detection(request):
    return render(request, 'detection/live_detection.html')