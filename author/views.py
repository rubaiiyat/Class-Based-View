from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from posts.models import Posts
from django.contrib.auth.views import LoginView, LogoutView


def Register(request):
    if request.user.is_authenticated:
        return redirect("profile")
    else:
        page = "Register"

        if request.method == "POST":
            form = forms.RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, "Account Registration Successfully")
                form.save()
                return redirect("register")

        else:
            form = forms.RegisterForm()
        return render(request, "Register.html", {"page": page, "form": form})


def userLogin(request):
    if request.user.is_authenticated:
        return redirect("profile")
    else:
        page = "Login"

        if request.method == "POST":
            userForm = AuthenticationForm(request=request, data=request.POST)

            if userForm.is_valid():
                name = request.POST["username"]
                userpass = request.POST["password"]
                user = authenticate(request, username=name, password=userpass)

                if user is not None:
                    messages.success(request, "Loggined Successfully")
                    login(request, user)
                    return redirect("profile")

            messages.warning(request, "Invalid username or password")
        else:
            userForm = AuthenticationForm()
        return render(request, "login.html", {"form": userForm, "page": page})


class userLoginView(LoginView):
    template_name = "register.html"

    def get_success_url(self) -> str:
        return reverse_lazy("profile")

    def form_valid(self, form):
        messages.success(self.request, "Logged In Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "Invalid Username or Password")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "login"
        return context


@login_required
def userProfile(request):
    page = "Profile"
    data = Posts.objects.filter(author=request.user)
    user_profile = request.user
    return render(
        request, "profile.html", {"form": user_profile, "page": page, "data": data}
    )


@login_required
def editProfile(request):
    page = "Edit Profile"

    if request.method == "POST":
        form = forms.editProfile(request.POST, instance=request.user)
        if form.is_valid():

            form.save()
            return redirect("profile")
    else:
        form = forms.editProfile(instance=request.user)
    return render(request, "editProfile.html", {"page": page, "form": form})


@login_required
def chngPass(request):
    page = "Change Password"
    if request.method == "POST":
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Password Updated Successfully")
            update_session_auth_hash(request, form.user)
            return redirect("profile")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "chngPass.html", {"page": page, "form": form})


def viewUserProfile(request, username):

    user_profile = get_object_or_404(User, username=username)
    user_post = Posts.objects.filter(author=user_profile)
    page = username
    return render(
        request,
        "user_profile.html",
        {"user_profile": user_profile, "page": page, "data": user_post},
    )


@login_required
def userLogout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("login")
