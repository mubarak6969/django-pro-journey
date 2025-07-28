from django.urls import path
from .views import mood_entry_view

urlpatterns = [
    path('', mood_entry_view, name='mood-form'),
]
