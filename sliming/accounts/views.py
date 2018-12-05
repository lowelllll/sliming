from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm
    return render(request, 'accounts/signup_form.html', {'form':form})


@login_required
def profile(request, user):
    if request.user.username != user:
        print(type(request.user), type(user))
        return redirect('index')

    User = get_user_model()
    author = User.objects.get(id=request.user.id)
    return render(request, 'accounts/mypage.html', {'author':author})