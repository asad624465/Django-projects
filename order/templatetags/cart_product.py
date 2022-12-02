from atexit import register
from django import template

from order.models import Cart,Order

register=template.Library()

@register.filter

def cart_view(user):
    cart=Cart.objects.filter(user=user,purchased=False)
    if cart.exists():
        return cart
    else:
        return ValueError("You haven't an active cart!")

@register.filter

def cart_total(user):
    total=Order.objects.filter(user=user,ordered=False)
    if total.exists():
        return total[0].get_totals()
    else:
        0

@register.filter

def cart_count(user):
    total_item=Order.objects.filter(user=user,ordered=False)
    if total_item.exists():
            return total_item[0].orderitems.count()
    else:
        0
    
