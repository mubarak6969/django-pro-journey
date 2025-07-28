from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MoodEntry

def mood_entry_view(request):
    if request.method == 'POST':
        mood = request.POST.get('mood')
        note = request.POST.get('note')
        MoodEntry.objects.create(mood=mood, note=note)
        messages.success(request, "Mood entry saved!")
        return redirect('mood-form')  # or use your named URL

    return render(request, 'tracker/mood_form.html')


def mood_history_view(request):
    mood_filter = request.GET.get('mood')  # get ?mood= from URL
    if mood_filter:
        entries = MoodEntry.objects.filter(mood=mood_filter).order_by('-date')
    else:
        entries = MoodEntry.objects.order_by('-date')
    
    return render(request, 'tracker/mood_history.html', {
        'entries': entries,
        'current_filter': mood_filter
    })
