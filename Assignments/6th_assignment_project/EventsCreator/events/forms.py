from django import forms
from .models import Event, User
from django.contrib.auth.forms import UserCreationForm


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
