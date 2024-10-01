from django.shortcuts import render, redirect
from .forms import CategoryForm


# Create your views here.
def category(request):
    page = "Category"

    if request.method == "POST":
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect("category")

    else:
        category_form = CategoryForm()
    return render(request, "category.html", {"page": page, "form": category_form})
