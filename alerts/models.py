from django.db import models
from detection.models import Detection


class Alert(models.Model):
    STATUS = [('new', 'New'), ('acknowledged', 'Acknowledged'), ('resolved', 'Resolved')]

    detection = models.ForeignKey(Detection, on_delete=models.CASCADE, related_name='alerts')
    severity = models.CharField(max_length=10, default='High')
    status = models.CharField(max_length=15, choices=STATUS, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alert {self.id} - {self.status}"