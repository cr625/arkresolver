from django import forms
from .models import Capture


class CaptureForm(forms.ModelForm):
    class Meta:
        model = Capture
        fields = ("parent_ark", "capture_ark_id", "warc", "manifest")
