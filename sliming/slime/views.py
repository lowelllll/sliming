from django.shortcuts import render, redirect
from .forms import SlimeForm

def add_slime(request):
    if request.method == 'POST':
        form = SlimeForm(request.POST, request.FILES)
        if form.is_valid():
            slime = form.save(commit=False)
            slime.shop = request.user.shop
            slime.save(commit=True)
            return redirect('shop:detail')
    else:
        form = SlimeForm()
    return render(request, 'slime/slime_form.html', {'form': form})