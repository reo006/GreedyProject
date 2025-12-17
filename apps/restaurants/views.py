from django.shortcuts import render

from .models import Restaurant


def search(request):
    query = request.GET.get('q')
    if query:
        restaurants = Restaurant.objects.filter(name__icontains=query)
    else:
        restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/search.html', {'restaurants': restaurants, 'query': query})

