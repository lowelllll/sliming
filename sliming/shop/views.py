from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# from django.views.generic import ListView
from .forms import ShopForm
from .models import Shop, Follow

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
        shop = Shop.objects.select_related('user').prefetch_related('slime_set', 'offline').get(name=shop)
        if request.user != shop.user:
            is_follow = Follow.objects.filter(requester=request.user.id, shop=shop.id)
        else:
            is_follow = None
    except Exception:
        raise Http404()
    return render(request, 'shop/shop_detail.html', {'shop':shop, 'is_follow': is_follow})


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
    return JsonResponse({'shops': list(shops)})


@csrf_exempt
def follow(request):
    requester_id = request.POST.get('requester', 0)
    shop_id = request.POST.get('shop', 0)

    obj, created = Follow.objects.get_or_create(
        requester=requester_id,
        shop=shop_id
    )
    action = 'unfollow'

    if not created:
        obj.delete()
        action = 'follow'

    return JsonResponse({'action': action})
