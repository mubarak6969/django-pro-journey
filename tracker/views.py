from django.shortcuts import render, redirect
from .models import MoodEntry

def mood_entry_view(request):
    if request.method == 'POST':
        mood = request.POST.get('mood')
        note = request.POST.get('note')
        MoodEntry.objects.create(mood=mood, note=note)
        return redirect('mood-form')
    
    return render(request, 'tracker/mood_form.html')
