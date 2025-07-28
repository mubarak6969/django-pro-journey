from django.db import models

class MoodEntry(models.Model):
    MOOD_CHOICES = [
        ('😄', 'Happy'),
        ('😐', 'Neutral'),
        ('😔', 'Sad'),
        ('😡', 'Angry'),
        ('😴', 'Tired'),
    ]
    
    mood = models.CharField(max_length=2, choices=MOOD_CHOICES)
    note = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)

    def _str_(self):
        return f"{self.mood} - {self.date}"