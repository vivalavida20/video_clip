from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Clip
from .form import ClipForm

def index(request):
    categories = Category.objects.all()
    clips = Clip.objects.all()

    return render(request, "video_clip/index.html", {"categories":categories, "clips":clips})

def new(request):
    if request.method == "POST":
        form = ClipForm(request.POST)
        if form.is_valid():
            clip = form.save()
            return redirect("index")
    else:
        form = ClipForm()
        return render(request, "video_clip/form.html", {"form":form})

def detail(request, pk):
    clip = Clip.objects.get(pk=pk)
    return render(request, "video_clip/detail.html", {"clip":clip})

def edit(request, pk):
    clip = get_object_or_404(Clip, pk=pk)

    if request.method == 'POST':
        form = ClipForm(request.POST, instance=clip)
        if form.is_valid():
            clip = form.save()
            return redirect(clip)
    else:
        form = ClipForm(instance=clip)
    return render(request, 'video_clip/form.html', {'form':form})


def delete(request, pk):
    clip = Clip.objects.get(pk=pk)
    clip.delete()

    return redirect('index')

def category(request, name):
    category = Category.objects.get(name=name)
    clips = Clip.objects.filter(category=category)

    return render(request, 'video_clip/category_detail.html', {'clips':clips, 'category':category})

