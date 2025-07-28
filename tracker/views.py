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
    mood_filter = request.GET.get('mood')  # Get ?mood= from URL
    if mood_filter:
        entries = MoodEntry.objects.filter(mood=mood_filter).order_by('-date')
    else:
        entries = MoodEntry.objects.order_by('-date')
    
    return render(request, 'tracker/mood_history.html', {
        'entries': entries,
        'current_filter': mood_filter
    })
