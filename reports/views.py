from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from accounts.models import User
from alerts.models import Alert
from detection.models import Detection, Transcription, ToxicWordLog


@login_required
def admin_dashboard(request):
    ctx = {
        'total_alerts': Alert.objects.count(),
        'harmful_count': Detection.objects.filter(label='harmful').count(),
        'normal_count': Detection.objects.filter(label='normal').count(),
        'authority_count': User.objects.filter(role='authority').count(),
        'recent_alerts': Alert.objects.order_by('-created_at')[:5],
    }
    return render(request, 'reports/admin_dashboard.html', ctx)


@login_required
def transcripts(request):
    return render(request, 'reports/transcripts.html', {'transcripts': Transcription.objects.all()})


@login_required
def toxic_words(request):
    return render(request, 'reports/toxic_words.html', {'words': ToxicWordLog.objects.all()})


@login_required
def reports(request):
    return render(request, 'reports/reports.html', {'incidents': Alert.objects.order_by('-created_at')})


@login_required
def system_settings(request):
    return render(request, 'reports/system_settings.html')