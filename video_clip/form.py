from django import forms
from .models import Clip

class ClipForm(forms.ModelForm):

    class Meta:
        model = Clip
        fields = ('title', 'video_url', 'memo', 'category',)