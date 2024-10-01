from django import forms
from .models import Posts


class postForm(forms.ModelForm):
    class Meta:

        model = Posts
        exclude = ["author"]
