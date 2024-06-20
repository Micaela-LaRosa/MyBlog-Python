from .models import Blog
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class UserEditForm(UserChangeForm):
    password = forms.CharField(
        help_text='',
        widget=forms.HiddenInput(), required=False
    )
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repit password", widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=["username", "email"]

    def clean_password2(self):

        print(self.cleaned_data)
        password1=self.cleaned_data["password1"]
        password2=self.cleaned_data["password2"]

        if password1 != password2:
            raise forms.ValidationError("The password did not match")
        return password2