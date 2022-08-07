from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from .forms import PostForm
from .models import Post

from logging import getLogger
log = getLogger(__name__)


def index(request):
    posts = Post.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except Exception(e):
                log.error("failed to save post: %s" % e)
    else:
        form = PostForm()
    return render(request, "index.html", {'posts': posts, 'form': form})


def show(request, id):
    post = Post.objects.get(id=id)
    return render(request,'show.html', {'post': post})


def edit(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("posts:show", post.id)
    else:
        form = PostForm(instance=post)
    return render(request,'edit.html', {'post': post, 'form': form})


def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect("/")
