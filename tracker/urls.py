from django.urls import path
from .views import mood_entry_view, mood_history_view

urlpatterns = [
    path('', mood_entry_view, name='mood-form'),
    path('history/', mood_history_view, name='mood-history'),
]
from django.urls import path
from .views import mood_entry_view, mood_history_view

urlpatterns = [
    path('', mood_entry_view, name='mood-form'),
    path('history/', mood_history_view, name='mood-history'),
]
