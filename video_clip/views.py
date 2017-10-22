from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Clip
from .form import ClipForm, CategoryForm

def send_categories():
    categories = Category.objects.all()

    return categories


def index(request):
    clips = Clip.objects.order_by('-created_at')

    return render(request, "video_clip/index.html", {"categories":send_categories(), "clips":clips})

def new(request):
    if request.method == "POST":
        form = ClipForm(request.POST)
        if form.is_valid():
            clip = form.save()
            return redirect("index")
    else:
        form = ClipForm()
        return render(request, "video_clip/form.html", {"categories":send_categories(), "form":form})

def detail(request, pk):
    clip = Clip.objects.get(pk=pk)
    return render(request, "video_clip/detail.html", {"categories":send_categories(), "clip":clip})

def edit(request, pk):
    clip = get_object_or_404(Clip, pk=pk)

    if request.method == 'POST':
        form = ClipForm(request.POST, instance=clip)
        if form.is_valid():
            clip = form.save()
            return redirect(clip)
    else:
        form = ClipForm(instance=clip)
    return render(request, 'video_clip/form.html', {"categories":send_categories(), 'form':form})


def delete(request, pk):
    clip = Clip.objects.get(pk=pk)
    clip.delete()

    return redirect('index')

def category(request, name):
    category = Category.objects.get(name=name)
    clips = Clip.objects.filter(category=category).order_by('-created_at')

    return render(request, 'video_clip/category_detail.html', {'clips':clips, 'category':category, "categories":send_categories()})

def new_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return redirect("index")
    else:
        form = CategoryForm()
    return render(request, "video_clip/category_form.html", {"categories":send_categories(), "form":form})

