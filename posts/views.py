from django.shortcuts import render, redirect, get_object_or_404
from .forms import postForm
from . import models
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def post(request):
    page = "Posts"
    if request.method == "POST":
        post_Form = postForm(request.POST)
        if post_Form.is_valid():
            post_Form.instance.author = request.user
            post_Form.save()
            return redirect("posts")

    else:
        post_Form = postForm()
    return render(request, "post.html", {"form": post_Form, "page": page})


def editPost(request, id):
    page = "Edit Post"
    posts = get_object_or_404(models.Posts, pk=id)

    if posts.author != request.user:
        return redirect("home")
    post_Form = postForm(instance=posts)

    if request.method == "POST":
        post_Form = postForm(request.POST, instance=posts)
        if post_Form.is_valid():
            post_Form.save()
            return redirect("profile")

    return render(request, "post.html", {"form": post_Form, "page": page})


def deletePost(request, id):
    posts = get_object_or_404(models.Posts, pk=id)
    if posts.author != request.user:
        return redirect("home")
    posts.delete()
    return redirect("home")
