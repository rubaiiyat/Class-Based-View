from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("register/", views.Register, name="register"),
    # path("login/", views.userLogin, name="login"),
    path("login/", views.userLoginView.as_view(), name="login"),
    path("profile/", views.userProfile, name="profile"),
    path("profile/edit/", views.editProfile, name="edit"),
    path("profile/edit/changepassword/", views.chngPass, name="changepassword"),
    # path("logout/", views.userLogout, name="logout"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("<str:username>/", views.viewUserProfile, name="view_profile"),
]
