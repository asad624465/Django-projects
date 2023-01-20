from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from store.models import Product
from order.models import Cart, Order

from coupon.forms import CouponCodeForm
from coupon.models import Coupon
from django.utils import timezone

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

def cartView(request):
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user,purchased = False)
        orders = Order.objects.filter(user=request.user, ordered = False)
        if carts.exists() and orders.exists():
            order = orders[0]
            coupon_form=CouponCodeForm(request.POST)
            if coupon_form.is_valid():
                current_time=timezone.now().date()
                code=coupon_form.cleaned_data.get('code')
                try:
                    coupon_obj=Coupon.objects.get(code=code)
                    if coupon_obj.valid_to >= current_time and coupon_obj.active_status==True:
                        get_discount=(coupon_obj.discount/100)*order.get_totals()
                        total_price_after_discount=order.get_totals()-get_discount
                        request.session['discount_amount']=get_discount
                        request.session['total_price_after_discount']=total_price_after_discount
                        request.session['coupon_code']=code
                        return redirect('order:cart')
                except Coupon.DoesNotExist:
                    coupon_obj = None
            request.session['discount_amount']=1700
            request.session['total_price_after_discount']=15300
            total_price_after_discount=request.session.get('total_price_after_discount')
            code=request.session.get('coupon_code')
            discount_amount=request.session.get('discount_amount')
            context={
                'carts':carts,
                'orders':orders[0],
                'coupon_form':coupon_form,
                'total_price_after_discount':total_price_after_discount,
                'discount_amount':discount_amount,
                'coupon_code':code,
            }
            return render(request,'frontend/cart_view.html',context);
        else:
            return render(request,'frontend/cart_view.html',{}); 
    else:
        return redirect('account:login')   
def removeItemFromCart(request, pk):
    item=get_object_or_404(Product, pk=pk)
    orders = Order.objects.filter(user=request.user,ordered=False)
    if orders.exists():
        order=orders[0]
        if order.orderitems.filter(item=item).exists():
            order_item=Cart.objects.filter(user=request.user, item=item, purchased=False)[0]
            order.orderitems.remove(order_item)
            order_item.delete()
            return redirect('order:cart')
        else:
            return redirect('order:cart')
    else:
        return redirect('order:cart')

def increaseItemOfCart(request,pk):
    item=get_object_or_404(Product,pk=pk)
    orders = Order.objects.filter(user=request.user, ordered=False)
    if orders.exists():
        order=orders[0]
        if order.orderitems.filter(item=item).exists():
            order_item=Cart.objects.filter(user=request.user,item=item,purchased=False)[0]
            if order_item.quantity >=1:
                order_item.quantity +=1
                order_item.save()
                return redirect('order:cart')
            else:
             return redirect('order:cart')   
        else:
            return redirect('store:index')
    else:
        return redirect('store:index')

def decreaseItemOfCart(request,pk):
    item=get_object_or_404(Product,pk=pk)
    orders=Order.objects.filter(user=request.user,ordered=False)
    if orders.exists():
        order=orders[0]
        if order.orderitems.filter(item=item).exists():
            order_item=Cart.objects.filter(item=item,user=request.user,purchased=False)[0]
            if order_item.quantity > 1:
               order_item.quantity -=1;
               order_item.save()
               return redirect('order:cart') 
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
                return redirect('store:index')  
        else:
            return redirect('store:index')
    else:
        return redirect('store:index');
            
    