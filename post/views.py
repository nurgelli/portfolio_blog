from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/post_list.html', {"posts": posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post/post_detail.html', {"post": post})

def post_create(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post:list')
    return render(request, 'post/post_create.html', {"form": form})

def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post:detail', id=post.id)
    return render(request, 'post/post_create.html', {"form": form})


def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        post.delete()
        return redirect('post:list')
    return render(request, 'post/confirm.html', {"post":post})