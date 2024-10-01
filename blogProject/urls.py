from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.Home, name="home"),
    path("category/<slug:category_slug>", views.Home, name="slug_category"),
    path("author/", include("author.urls")),
    path("category/", include("categories.urls")),
    path("posts/", include("posts.urls")),
]
