from django import forms
from .models import *

class ResgistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'face_id',
            'name',
            'email'
        ]
        widgets = {'face_id':forms.HiddenInput()}