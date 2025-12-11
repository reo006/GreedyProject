from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils import timezone
from datetime import datetime, timedelta
from django.db import OperationalError
from django.shortcuts import render, redirect, get_object_or_404  # ← これが必要！
from .models import Delivery, Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def purchase_view(request):
    cart = get_cart(request.user)

    if cart.items.count() == 0:
        return redirect("cart")

    return render(request, "core/purchase.html", {"cart": cart})



# ===========================
# 🔹 カート取得
# ===========================
def get_cart(user):
    cart, created = Cart.objects.get_or_create(user=user)
    return cart


# ===========================
# 🔹 カートに追加
# ===========================
@login_required
def add_to_cart(request, item_id):
    cart = get_cart(request.user)

    MENU_DATA = {
        "yasai": {"name": "ヘルシー野菜プレート", "price": 800, "img": "yasai.jpg"},
        "suteki": {"name": "ジューシーステーキセット", "price": 1500, "img": "suteki.jpg"},
        "susij": {"name": "彩り寿司御膳", "price": 1800, "img": "susi.jpg"},
        "pafe": {"name": "デザートパフェ", "price": 700, "img": "pafe.jpg"},
    }

    item = MENU_DATA.get(item_id)
    if not item:
        raise Http404("商品が存在しません")

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        name=item["name"],
        defaults={"price": item["price"], "image": item["img"], "quantity": 1},
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart")


# ===========================
# 🔹 カート画面
# ===========================
@login_required
def cart_view(request):
    cart = get_cart(request.user)
    return render(request, "core/cart.html", {"cart": cart})


# ===========================
# 🔹 商品詳細ページ
# ===========================
def menu_detail(request, item_name):
    menu_data = {
        'yasai': {
            'title': '🌿 ヘルシー野菜プレート',
            'desc': '新鮮な地元野菜を使った健康志向プレートです。',
             "img": "yasai.jpg",
            'price': 800
        },
        'suteki': {
            'title': '🥩 ジューシーステーキセット',
            'desc': '国産牛をじっくり焼き上げたボリューム満点の一品。',
            'img': "suteki.jpg",
            'price': 1500
        },
        'susij': {
            'title': '🍣 彩り寿司御膳',
            'desc': '新鮮なネタを贅沢に使った寿司御膳。',
            'img': "susi.jpg",
            'price': 1800
        },
        'pafe': {
            'title': '🍓 デザートパフェ',
            'desc': '旬のフルーツをふんだんに使った甘美なデザート。',
            'img': "pafe.jpg",
            'price': 700
        },
    }

    if item_name not in menu_data:
        raise Http404("指定されたメニューは存在しません。")

    return render(request, 'core/menu_detail.html', {
        **menu_data[item_name],
        "item_id": item_name,  # カート追加用
    })


    if item_name not in menu_data:
        raise Http404("指定されたメニューは存在しません")

    data = menu_data[item_name]

    return render(request, "core/menu_detail.html", {
        "title": data["title"],
        "desc": data["desc"],
        "img": data["img"],
        "item_id": item_name,
    })


# ===========================
# 🔹 ホーム画面
# ===========================
@ensure_csrf_cookie
def home(request):
    today = timezone.localdate()
    delivery = None
    delivery_time = (datetime.now() + timedelta(hours=1)).strftime('%H:%M')

    if request.user.is_authenticated:
        try:
            delivery, _ = Delivery.objects.get_or_create(user=request.user, date=today)
            username = request.user.username
        except OperationalError:
            delivery = None
            username = "ゲスト"
    else:
        username = "ゲスト"

    return render(request, "core/home.html", {
        "delivery": delivery,
        "delivery_time": delivery_time,
        "username": username,
    })


# ===========================
# 🔹 配達キャンセル
# ===========================
@login_required
@require_POST
def cancel_delivery(request):
    today = timezone.localdate()
    delivery, _ = Delivery.objects.get_or_create(user=request.user, date=today)
    delivery.canceled = True
    delivery.canceled_at = timezone.now()
    delivery.save()
    return JsonResponse({'status': 'ok', 'canceled': True})


# ===========================
# 🔹 配達復元
# ===========================
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


# ===========================
# 🔹 商品検索
# ===========================
def search(request):
    q = request.GET.get("q", "")
    return render(request, "core/search.html", {"query": q})

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
def purchase(request):
    cart = get_cart(request.user)
    return render(request, "core/purchase.html", {"cart": cart})

@login_required
def add_to_cart(request, item_id):
    cart = get_cart(request.user)

    MENU_DATA = {
        "yasai": {"name": "ヘルシー野菜プレート", "price": 800, "img": "images/yasai.jpg"},
        "suteki": {"name": "ジューシーステーキセット", "price": 1500, "img": "images/suteki.jpg"},
        "susij": {"name": "彩り寿司御膳", "price": 1800, "img": "images/susi.jpg"},
        "pafe": {"name": "デザートパフェ", "price": 700, "img": "images/pafe.jpg"},
    }

    item = MENU_DATA.get(item_id)

    if request.method == "POST":
        qty = int(request.POST.get("quantity", 1))

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            name=item["name"],
            defaults={"price": item["price"], "image": item["img"], "quantity": qty},
        )

        if not created:
            cart_item.quantity += qty
            cart_item.save()

    return redirect("cart")

@login_required
def purchase_complete(request):
    cart = get_cart(request.user)

    # カートを空にする
    cart.items.all().delete()

    return render(request, "core/purchase_complete.html")

@login_required
def update_cart_quantity(request, item_id):
    if request.method == "POST":
        new_qty = int(request.POST.get("quantity", 1))
        cart = get_cart(request.user)

        item = CartItem.objects.get(id=item_id, cart=cart)
        item.quantity = max(new_qty, 1)
        item.save()

    return redirect("cart")

@login_required
def delete_cart_item(request, item_id):
    cart = get_cart(request.user)
    item = CartItem.objects.get(id=item_id, cart=cart)
    item.delete()
    return redirect("cart")
@login_required
def purchase_view(request):
    cart = get_cart(request.user)

    # カートが空なら購入できない
    if cart.items.count() == 0:
        return render(request, "core/purchase.html", {
            "cart": cart,
            "error": "カートに商品がありません。"
        })

    if request.method == "POST":
        # 本当は決済処理を書く場所（今回は省略）
        cart.items.all().delete()  # 購入完了したらカートを空にする

        return render(request, "core/purchase_done.html")

    return render(request, "core/purchase.html", {"cart": cart})





