from django.shortcuts import render
from .models import Category, Clip

def index(request):
    categories = Category.objects.all()
    clips = Clip.objects.all()

    return render(request, "video_clip/index.html", {"categories":categories, "clips":clips})
