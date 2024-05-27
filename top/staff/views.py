from django.shortcuts import render, redirect
from store.models import *
from .forms import OrderForm, ProductForm


def home(request):
    orders = Order.objects.all()
    action = request.GET.get('filter')
    if action == 'new':
        orders = orders.filter(status='Создан')
    elif action == 'get':
        orders = orders.filter(status='Принят в работу')
    elif action == 'send':
        orders = orders.filter(status='В пути')
    elif action == 'done':
        orders = orders.filter(status='Доставлен')
    return render(request, 'admin.html', {'orders': orders})


def order(request, pk):
    order_data = Order.objects.get(pk=pk)
    return render(request, 'order.html', {'order': order_data})


def order_edit(request, pk):
    order_data = Order.objects.get(pk=pk)
    form = OrderForm(request.POST or None, instance=order_data)
    if form.is_valid():
        form.save()
        return redirect('staff:order', pk=pk)
    return render(request, 'order_edit.html', {'form': form})


def add_product(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('staff:home')
    print(40)
    return render(request, 'add_product.html', {'form': form})
