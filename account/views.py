from django.shortcuts import render
from  django.http import HttpResponse  

from account.forms import RegistrationForm
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
