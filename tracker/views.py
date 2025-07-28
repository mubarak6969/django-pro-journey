from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MoodEntry

def mood_entry_view(request):
    if request.method == 'POST':
        try:
            mood = request.POST.get('mood')
            note = request.POST.get('note')

            # Validate form data
            if not mood:
                messages.error(request, "Mood is required.")
                return redirect('mood-form')

            # Save to database
            MoodEntry.objects.create(mood=mood, note=note)

            # Show success message
            messages.success(request, "Mood entry saved successfully!")

            return redirect('mood-form')

        except Exception as e:
            # Print error in Render logs
            import traceback
            print("❌ ERROR OCCURRED:", e)
            traceback.print_exc()

            # Optionally show error on page (dev only)
            messages.error(request, f"Something went wrong: {e}")
            return render(request, 'tracker/mood_form.html', {'error': str(e)})

    # GET request
    return render(request, 'tracker/mood_form.html')
