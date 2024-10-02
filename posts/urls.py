from django.urls import path, include
from . import views

urlpatterns = [
    # path("", views.post, name="posts"),
    path("", views.addPostCreateView.as_view(), name="posts"),
    # path("edit/<int:id>/", views.editPost, name="edit"),
    path("edit/<int:id>/", views.editPostView.as_view(), name="edit"),
    # path("delete/<int:id>/", views.deletePost, name="delete"),
    path("delete/<int:id>/", views.deletePostView.as_view(), name="delete"),
    path("details/<int:id>/", views.detailPostView.as_view(), name="details"),
]
