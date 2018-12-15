import re
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import SlimeForm
from .models import Slime
from .module.slime import get_content


def add_slime(request):
    if request.method == 'POST':
        form = SlimeForm(request.POST, request.FILES)
        if form.is_valid():
            slime = form.save(commit=False)
            slime.shop = request.user.shop
            video_link = get_content(form.cleaned_data['video_link'])

            if not video_link:
                messages.error(request, '동영상이 개제되어있는 게시글이 아닙니다.',)
                return redirect('slime:add')

            slime.video_link = video_link
            slime.status = 1
            slime.save()
            return redirect('shop:detail', shop=request.user.shop)
    else:
        form = SlimeForm()
    return render(request, 'slime/slime_form.html', {'form': form})


def modify_slime(request, id):
    slime = get_object_or_404(Slime, id=id)
    if request.method == 'POST':
        form = SlimeForm(request.POST, request.FILES, instance=slime)
        if form.is_valid():
            slime = form.save(commit=False)

            pattern = r'^https://scontent-icn1-1.cdninstagram.com/.'
            if not re.match(pattern, form.cleaned_data['video_link']):
                video_link = get_content(form.cleaned_data['video_link'])
                if not video_link:
                    messages.error(request, '동영상이 개제되어있는 게시글이 아닙니다.',)
                    return redirect('slime:modify')
                slime.video_link = video_link

            slime.save()
            return redirect('slime:detail', id=slime.id)
    else:
        form = SlimeForm(instance=slime)
    return render(request, 'slime/slime_form.html', {'form': form})


def detail_slime(request, id):
    slime = get_object_or_404(Slime, id=id)
    return render(request, 'slime/slime.html', {'slime': slime})
