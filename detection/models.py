from django.db import models


class AudioClip(models.Model):
    file = models.FileField(upload_to='audio/')
    device_id = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=100, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return f"Clip {self.id} - {self.location}"


class Transcription(models.Model):
    clip = models.ForeignKey(AudioClip, on_delete=models.CASCADE, related_name='transcriptions')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transcript of clip {self.clip_id}"


class Detection(models.Model):
    LABELS = [('harmful', 'Harmful'), ('normal', 'Normal')]

    clip = models.ForeignKey(AudioClip, on_delete=models.CASCADE, related_name='detections')
    transcription = models.OneToOneField(Transcription, on_delete=models.CASCADE, related_name='detection')
    label = models.CharField(max_length=10, choices=LABELS)
    confidence = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.label} ({self.confidence:.2f})"


class ToxicWordLog(models.Model):
    clip = models.ForeignKey(AudioClip, on_delete=models.CASCADE, related_name='toxic_words')
    toxic_word = models.CharField(max_length=50)
    detected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.toxic_word