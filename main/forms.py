from .models import Thread
from django.forms import ModelForm, TextInput


class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = ["participants"]
