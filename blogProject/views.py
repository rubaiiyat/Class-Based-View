from django.shortcuts import render
from posts.models import Posts
from categories.models import Category


def Home(request, category_slug=None):
    page = "Home"
    data = Posts.objects.all()

    if category_slug is not None:
        category = Category.objects.get(slug=category_slug)
        data = Posts.objects.filter(category=category)

    categories = Category.objects.all()
    return render(
        request, "home.html", {"page": page, "data": data, "category": categories}
    )
