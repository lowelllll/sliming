from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('last_name', 'first_name')

    profile_image = forms.ImageField(label='프로필 사진')
    nickname = forms.CharField(label='닉네임')

    # CHOICES = (('Option 1', 'Option 1'), ('Option 2', 'Option 2'),)
    CHOICES = ((str(year)+'-1-1 00:00:00', str(year)) for year in range(2018, 1969, -1))
    birth_year = forms.ChoiceField(choices=tuple(CHOICES))

    def save(self):
        user = super().save()
        profile= Profile.objects.create(
            user=user,
            profile_image=self.cleaned_data['profile_image'],
            nickname=self.cleaned_data['nickname'],
            birth_year=self.cleaned_data['birth_year']
        )
        return user
