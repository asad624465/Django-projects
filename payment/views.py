from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from account.models import Profile
User=get_user_model()
#import Models
from payment.models import BillingAddress
from payment.forms import BillingAddressForm,PaymentForms
from order.models import Cart, Order
from django.conf import settings
import json
#view import
from django.views.generic import TemplateView
#import payment gateway here
#from sslcommerz_python.payment import SSLCSession
from sslcommerz_lib import SSLCOMMERZ
from decimal import Decimal
#from sslcommerz_lib import SSLCOMMERZ 
from django.views.decorators.csrf import csrf_exempt

class CheckoutTemplateView(TemplateView):
    def get(self, request, *args, **kwargs):
        bl_address=BillingAddress.objects.get_or_create(user=request.user or None)
        bl_address=bl_address[0]
        form=BillingAddressForm(instance=bl_address)
        payment_method=PaymentForms()
        order_list=Order.objects.filter(user=request.user,ordered=False)
        order_items=order_list[0].orderitems.all()
        total_amount=order_list[0].get_totals()
        context={
            'billling_addresss':form,
            'order_items':order_items,
            'total_amount':total_amount,
            'payment_method':payment_method,
        }
        return render(request,'frontend/checkout.html', context)

    def post(self, request, *args, **kwargs):
        bl_address=BillingAddress.objects.get_or_create(user=request.user or None)
        bl_address=bl_address[0]
        form=BillingAddressForm(instance=bl_address)
        payment_object=Order.objects.filter(user=request.user,ordered=False)[0]
        payment_form=PaymentForms(instance=payment_object)

        if request.method=='post' or request.method=='POST':
            form=BillingAddressForm(request.POST,instance=bl_address)
            pay_form=PaymentForms(request.POST,instance=payment_object)
            form.save()
            pay_form=pay_form.save()
            if not bl_address.is_fully_filled():
                return redirect('checkout')
            
            #Start here cash on delivery payment proccess
            if pay_form.payment_method=='Cash on Delivery':
                order=Order.objects.filter(user=request.user, ordered=False)[0]
                order.ordered=True
                order.orderId=order.id
                order.paymentId='Cash on Delivery'
                order.save()
                cartItesms=Cart.objects.filter(user=request.user, purchased=False)
                for item in cartItesms:
                    item.purchased=True
                    item.save()
                return redirect('store:index')

            if pay_form.payment_method=='SSLcommerz':
                store_id=settings.STORE_ID
                store_pass=settings.STORE_PASS
                setting_s = { 'store_id': store_id, 'store_pass': store_pass, 'issandbox': True }
                sslcz = SSLCOMMERZ(setting_s)
                user_info=request.user
                form=BillingAddress.objects.filter(user=request.user)[0]
                order_list=Order.objects.filter(user=request.user,ordered=False)[0]
                order_items=order_list.orderitems.all()
                totalOrderItem=order_list.orderitems.count()
                totalAmount=order_list.get_totals()
                status_url=request.build_absolute_uri(reverse('payment:status'))
                
                
                post_body = {}
                post_body['total_amount'] = totalAmount
                post_body['currency'] = "BDT"
                post_body['tran_id'] = order_list.id
                post_body['success_url'] = status_url
                post_body['fail_url'] = status_url
                post_body['cancel_url'] = status_url
                post_body['emi_option'] = 0
                post_body['cus_name'] = request.user.profile.full_name
                post_body['cus_email'] = request.user.profile.email
                post_body['cus_phone'] = request.user.profile.phone
                post_body['cus_add1'] = request.user.profile.address
                post_body['cus_city'] = request.user.profile.city
                post_body['cus_country'] = request.user.profile.country
                post_body['shipping_method'] = "YES"
                post_body['multi_card_name'] = ""
                post_body['num_of_item'] = totalOrderItem
                post_body['product_name'] = order_items
                post_body['product_category'] = "clothing"
                post_body['product_profile'] = "general"
                post_body['ship_name'] = form.first_name
                post_body['ship_add1'] = form.address_one
                post_body['ship_add2'] = form.address_two
                post_body['ship_city'] = form.city
                post_body['ship_state'] = form.city
                post_body['ship_postcode'] = form.zipcode
                post_body['ship_country'] = "Bangladesh"
                response = sslcz.createSession(post_body) # API response
                print("------------------")
                #print(response)
                print("------------------")
                return redirect(response['GatewayPageURL'])
            return redirect('order:cart')
        return redirect('order:cart')

@csrf_exempt
def sslc_status(request):
    if request.method=='post' or request.method=='POST':
        payment_data=request.POST
        status=payment_data['status']
        print(status)
        if status == 'VALID':
            tran_id=payment_data['tran_id']
            val_id=payment_data['val_id']
            return HttpResponseRedirect(reverse('payment:sslc_complete',kwargs={'val_id':val_id,'tran_id':tran_id}))
        if status == 'FAILED':
            return redirect('payment:checkout')
    return render(request,'status.html')

def sslc_complete(request,val_id,tran_id):
    order=Order.objects.filter(user=request.user, ordered=False)[0]
    order.ordered=True
    order.orderId=val_id
    order.paymentId=tran_id
    order.save()
    cartItesms=Cart.objects.filter(user=request.user, purchased=False)
    for item in cartItesms:
        item.purchased=True
        item.save()
    return redirect('store:index')
# Create your views here.
