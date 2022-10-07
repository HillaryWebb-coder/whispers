from django import forms

from .models import Follow, Profile


class FollowUserForm(forms.ModelForm):

    class Meta:
        model = Follow
        fields = ("user_to",)
        widgets = {"user_to": forms.HiddenInput()}


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("avatar",)
