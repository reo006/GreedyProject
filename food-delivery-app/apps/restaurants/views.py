from django.shortcuts import render
from .models import Restaurant

def search_restaurants(request):
    query = request.GET.get('q')
    if query:
        restaurants = Restaurant.objects.filter(name__icontains=query)
    else:
        restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/search.html', {'restaurants': restaurants})

def search(request):
    # search_restaurants の別名
    return search_restaurants(request)

def cart(request):
    # カート表示ビュー
    return render(request, 'restaurants/cart.html')
