from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Alert


@login_required
def authority_dashboard(request):
    ctx = {
        'new_count': Alert.objects.filter(status='new').count(),
        'ack_count': Alert.objects.filter(status='acknowledged').count(),
        'resolved_count': Alert.objects.filter(status='resolved').count(),
        'latest_alerts': Alert.objects.order_by('-created_at')[:5],
    }
    return render(request, 'alerts/authority_dashboard.html', ctx)


@login_required
def alerts(request):
    return render(request, 'alerts/alerts.html', {'alerts': Alert.objects.order_by('-created_at')})


@login_required
def alert_detail(request, pk):
    return render(request, 'alerts/alert_detail.html')


@login_required
def history(request):
    return render(request, 'alerts/history.html', {'alerts': Alert.objects.order_by('-created_at')})