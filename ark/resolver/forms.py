from django import forms
from .models import Capture


class CaptureForm(forms.ModelForm):
    class Meta:
        model = Capture
        fields = ["capture_uri"]
