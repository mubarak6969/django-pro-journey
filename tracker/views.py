from django.shortcuts import render, redirect
from .models import MoodEntry

def mood_entry_view(request):
    if request.method == 'POST':
        mood = request.POST.get('mood')
        note = request.POST.get('note', '')
        if mood:
            MoodEntry.objects.create(mood=mood, note=note)
            return redirect('mood-history')  # Redirect after submission
    return render(request, 'tracker/mood_form.html')

def mood_history_view(request):
    moods = MoodEntry.objects.all().order_by('-timestamp')
    return render(request, 'tracker/mood_history.html', {'moods': moods})
