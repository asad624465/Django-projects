from django.shortcuts import render, redirect
from  django.http import HttpResponse 
from account.forms import RegistrationForm,ProfileForm 
#authentication info
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from order.models import Cart,Order
from payment.models import BillingAddress
from payment.forms import BillingAddressForm
from account.models import Profile
from django.views.generic import TemplateView
def register(req):
    if req.user.is_authenticated:
        return HttpResponse('you are already authenticate user')
    else:
        form =RegistrationForm()
        if req.method=='post' or req.method=='POST':
            form =RegistrationForm(req.POST)
            if form.is_valid():
                form.save()
                return HttpResponse('Your account has been created!')

    context={'form':form}
    return render(req,'backend/register.html',context)

def Customerlogin(req):
    if req.user.is_authenticated:
        return HttpResponse('You are logged in!')
    else:
        if req.method=="POST" or req.method=="post":
            username=req.POST.get('username')
            password=req.POST.get('password')
            customer =authenticate(req,username=username,password=password)
            if customer is not None:
                login(req,customer)
                return HttpResponse('You are logged successfully!')
            else:
                return HttpResponse('404')
    return render (req,'backend/login.html')

class profileViews(TemplateView):
    def get(self,request,*args, **kwargs):
        orders=Order.objects.filter(user=request.user,ordered=True)
        context={
            'orders':orders,
        }
        return render (request,'frontend/profile.html',context)

    def post(self,request,*args, **kwargs):
        pass
class myAccountInfo(TemplateView):
    def get(self,request,*args, **kwargs):
        accountAddress=Profile.objects.get(user=request.user)
        accountAddress_form=ProfileForm(instance=accountAddress)
        context={
            'account_info':accountAddress_form,
        }
        return render (request,'frontend/myAccountInfo.html',context)

    def post(self,request,*args, **kwargs):
        if request.method=='POST' or request.method=='post':
            accountAddress=Profile.objects.get(user=request.user)
            accountAddress_form=ProfileForm(request.POST,instance=accountAddress)
            if accountAddress_form.is_valid():
                accountAddress_form.save()
                return redirect('account:my-account-information')
class myBillingInfo(TemplateView):
    def get(self,request,*args, **kwargs):
        billingAddress=BillingAddress.objects.get(user=request.user)
        billingAddress_form=BillingAddressForm(instance=billingAddress)
        context={
            'billling_addresss':billingAddress_form,
        }
        return render (request,'frontend/myBillingInfo.html',context)

    def post(self,request,*args, **kwargs):
        if request.method=='POST' or request.method=='post':
            billingAddress=BillingAddress.objects.get(user=request.user)
            billingAddress_form=BillingAddressForm(request.POST,instance=billingAddress)
            if billingAddress_form.is_valid():
                billingAddress_form.save()
                return redirect('account:my-billing-information')
            