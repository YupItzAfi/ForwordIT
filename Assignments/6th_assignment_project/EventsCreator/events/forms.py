from django import forms
from .models import Event, Users, Refund
from django.contrib.auth.forms import UserCreationForm
from django.apps import apps


class CreateObjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        model_name = kwargs.pop('model_name')
        super(CreateObjectForm, self).__init__(*args, **kwargs)

    class Meta:
        model = apps.get_model('events', 'Venue')
        fields = "__all__"


class RefundForm(forms.ModelForm):
    class Meta:
        model = Refund
        fields = "__all__"


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"


class CreateUserForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']
