from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("register/", views.Register, name="register"),
    path("login/", views.userLogin, name="login"),
    path("profile/", views.userProfile, name="profile"),
    path("profile/edit/", views.editProfile, name="edit"),
    path("profile/edit/changepassword/", views.chngPass, name="changepassword"),
    path("logout/", views.userLogout, name="logout"),
    path("<str:username>/", views.viewUserProfile, name="view_profile"),
]
