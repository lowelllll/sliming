from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('last_name', 'first_name', 'email')

    profile_image = forms.ImageField(label='프로필 사진')
    nickname = forms.CharField(label='닉네임')

    def save(self):
        user = super().save()
        profile= Profile.objects.create(user=user, profile_image=self.cleaned_data['profile_image'], nickname=self.cleaned_data['nickname'])
        return user
