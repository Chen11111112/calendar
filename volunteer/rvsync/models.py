# models.py
from django.db import models

class Event(models.Model):
    IDENTITY_CHOICES = [
        ("h", "🦔"),
        ("t", "🦕"),
        ("both", "兩個人"),
    ]

    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    identity = models.CharField(
        max_length=10,
        choices=IDENTITY_CHOICES,
        default="t"
    )

    def __str__(self):
        return f"{self.title} ({self.get_identity_display()})"
