from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404
from django.contrib.auth.decorators import login_required
# from django.views.generic import ListView
from .forms import ShopForm
from .models import Shop

@login_required
def create_shop(request):
    if request.method == 'POST':
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.user = request.user
            shop.status = False
            shop.save()
            return redirect('/')
    else:
        form = ShopForm()
    return render(request, 'shop/shop_form.html', {'form':form})


def detail_shop(request, shop):
    try:
        shop = Shop.objects.prefetch_related('offline').get(name=shop)
    except Exception:
        raise Http404()
    return render(request, 'shop/shop_detail.html', {'shop':shop})


def list_shop(request):
    """
    샵 리스트 반환
    :param request:
    :return:
    """
    order = request.GET.get('order', '-grade')
    shops = Shop.objects.filter(status=True).order_by(order)[:50] # 오픈중인 슬라임 마켓
    return render(request, 'shop/shop_list.html', {'shops': shops})


def more_shops(request):
    """
    현재 open되어있는 샵의 목록.
    무한스크롤 위함
    :param request:
    :return:
    """
    page = request.GET.get('page', 2)
    order = request.GET.get('order', '-grade')
    limit = 50
    offset = (page-1) * limit
    shops = Shop.objects.all().order_by(order)[offset:offset+limit].values()# 평점이 높은 순
    return JsonResponse(list(shops))

