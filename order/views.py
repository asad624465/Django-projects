from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from store.models import Product
from order.models import Cart, Order

def addToCart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_item=Cart.objects.get_or_create(item=item,user=request.user, purchased=False)
    order_data=Order.objects.filter(user=request.user,ordered=False)
    if order_data.exists():
        order=order_data[0]
        if order.orderitems.filter(item=item).exists():
            color=request.POST.get('color')
            qty=request.POST.get('qty')
            size=request.POST.get('size')
            print(color)
            if qty:
                order_item[0].quantity += int(qty)
            else:
                order_item[0].quantity += 1
            order_item[0].color = color
            order_item[0].size = size
            order_item[0].save()
            return redirect('store:index')
        else:
            color=request.POST.get('color')
            size=request.POST.get('size')
            print(size)
            order_item[0].color = color
            order_item[0].size = size
            order.orderitems.add(order_item[0])
            return redirect('store:index')
    else:
        order=Order(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        return redirect('store:index')