from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.post, name="posts"),
    path("edit/<int:id>/", views.editPost, name="edit"),
    path("delete/<int:id>/", views.deletePost, name="delete"),
]
