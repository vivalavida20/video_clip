from django import forms
from .models import Clip, Category

class ClipForm(forms.ModelForm):

    class Meta:
        model = Clip
        fields = ('title', 'video_url', 'memo', 'category',)

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name', 'slug', 'parent',)