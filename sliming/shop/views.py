from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ShopForm
from .models import Shop

@login_required
def create_shop(request):
    if request.method == 'POST':
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.user = request.user
            shop.is_open = False
            shop.save()
            return redirect('/')
    else:
        form = ShopForm()
    return render(request, 'shop/shop_form.html', {'form':form})


@login_required
def detail_shop(request, shop):
    shop = Shop.objects.prefetch_related('slime_set').get(name=shop)
    return render(request, 'shop/shop_detail.html', {'shop':shop})