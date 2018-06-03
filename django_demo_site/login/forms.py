from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ('username', )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        fields = ('username', 'email', )


