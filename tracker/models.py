from django.db import models

class MoodEntry(models.Model):
    mood = models.CharField(max_length=100)
    note = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mood} at {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
