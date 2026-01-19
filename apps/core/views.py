from datetime import datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST

from .models import Cart, CartItem, Delivery


MENU_DATA = {
    "yasai": {"name": "ヘルシー野菜プレート", "price": 800, "img": "yasai.jpg"},
    "suteki": {"name": "ジューシーステーキセット", "price": 1500, "img": "suteki.jpg"},
    "susij": {"name": "彩り寿司御膳", "price": 1800, "img": "susi.jpg"},
    "pafe": {"name": "デザートパフェ", "price": 700, "img": "pafe.jpg"},
}


def get_cart(user):
    cart, _ = Cart.objects.get_or_create(user=user)
    return cart


@ensure_csrf_cookie
def home(request):
    today = timezone.localdate()
    delivery = None
    delivery_time = (datetime.now() + timedelta(hours=1)).strftime('%H:%M')

    if request.user.is_authenticated:
        delivery, _ = Delivery.objects.get_or_create(user=request.user, date=today)
        username = request.user.username
    else:
        username = "ゲスト"

    return render(
        request,
        "core/home.html",
        {
            "delivery": delivery,
            "delivery_time": delivery_time,
            "username": username,
        },
    )


@login_required
def cart_view(request):
    cart = get_cart(request.user)
    return render(request, "core/cart.html", {"cart": cart})


def menu_detail(request, item_name):
    item = MENU_DATA.get(item_name)
    if not item:
        raise Http404("指定されたメニューは存在しません。")

    return render(
        request,
        "core/menu_detail.html",
        {
            "title": item["name"],
            "desc": item.get("desc", ""),
            "img": item["img"],
            "item_id": item_name,
            "price": item["price"],
        },
    )


@login_required
def add_to_cart(request, item_id):
    cart = get_cart(request.user)
    item = MENU_DATA.get(item_id)
    if not item:
        raise Http404("商品が存在しません")

    quantity = int(request.POST.get("quantity", 1)) if request.method == "POST" else 1
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        name=item["name"],
        defaults={"price": item["price"], "image": item["img"], "quantity": quantity},
    )
    if not created:
        cart_item.quantity += quantity
        cart_item.save()

    return redirect("cart")


@login_required
@require_POST
def cart_increase(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.quantity += 1
    item.save()
    return redirect("cart")


@login_required
@require_POST
def cart_decrease(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect("cart")


@login_required
@require_POST
def cart_delete(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    return redirect("cart")


@login_required
@require_POST
def update_cart_quantity(request, item_id):
    new_qty = int(request.POST.get("quantity", 1))
    cart = get_cart(request.user)
    item = get_object_or_404(CartItem, id=item_id, cart=cart)
    item.quantity = max(new_qty, 1)
    item.save()
    return redirect("cart")


@login_required
@require_POST
def delete_cart_item(request, item_id):
    cart = get_cart(request.user)
    item = get_object_or_404(CartItem, id=item_id, cart=cart)
    item.delete()
    return redirect("cart")


@login_required
def purchase(request):
    cart = get_cart(request.user)
    if cart.items.count() == 0:
        return redirect("cart")

    if request.method == "POST":
        cart.items.all().delete()
        return render(request, "core/purchase_complete.html")

    return render(request, "core/purchase.html", {"cart": cart})


@login_required
def purchase_complete(request):
    return render(request, "core/purchase_complete.html")


@login_required
@require_POST
def cancel_delivery(request):
    today = timezone.localdate()
    delivery, _ = Delivery.objects.get_or_create(user=request.user, date=today)
    delivery.canceled = True
    delivery.canceled_at = timezone.now()
    delivery.save()
    return JsonResponse({'status': 'ok', 'canceled': True})


@login_required
@require_POST
def restore_delivery(request):
    today = timezone.localdate()
    try:
        delivery = Delivery.objects.get(user=request.user, date=today)
    except Delivery.DoesNotExist:
        return JsonResponse({'status': 'ok', 'canceled': False})

    delivery.canceled = False
    delivery.canceled_at = None
    delivery.save()
    return JsonResponse({'status': 'ok', 'canceled': False})


def search(request):
    q = request.GET.get("q", "")
    return render(request, "core/search.html", {"query": q})

