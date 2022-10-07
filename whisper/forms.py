from django import forms

from .models import Whisper


class WhisperForm(forms.ModelForm):
    class Meta:
        model = Whisper
        fields = ("body",)
