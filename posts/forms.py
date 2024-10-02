from django import forms
from .models import Posts, CommnetPost


class postForm(forms.ModelForm):
    class Meta:

        model = Posts
        exclude = ["author"]


class commentForm(forms.ModelForm):
    class Meta:
        model = CommnetPost
        fields = ["content"]
