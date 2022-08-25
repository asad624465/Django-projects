from django.shortcuts import render
from  django.http import HttpResponse 
from account.forms import RegistrationForm 
#authentication info
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
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