from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order
from .forms import OrderForm

@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('orders:confirm_order', order_id=order.id)
    else:
        form = OrderForm()
    return render(request, 'orders/create_order.html', {'form': form})

@login_required
def confirm_order(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, 'orders/confirm.html', {'order': order})