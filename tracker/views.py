from django.shortcuts import render, redirect
from .models import MoodEntry

# Existing view
def mood_entry_view(request):
    if request.method == 'POST':
        mood = request.POST.get('mood')
        note = request.POST.get('note')
        MoodEntry.objects.create(mood=mood, note=note)
        return redirect('mood-form')
    
    return render(request, 'tracker/mood_form.html')

# 🔹 New view to list all entries
def mood_history_view(request):
    entries = MoodEntry.objects.order_by('-date')
    return render(request, 'tracker/mood_history.html', {'entries': entries})
