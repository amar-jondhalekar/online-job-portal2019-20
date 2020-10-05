from django import forms
from .models import JobPosts,Resume
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
class JobImageForm(forms.ModelForm):
    class Meta:
        model= JobPosts
        fields= ['image']

class ResumeForm(forms.ModelForm):
    class Meta:
        model=Resume
        fields=['resume']

