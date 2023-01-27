from django.shortcuts import render
from django.http import HttpResponseRedirect
from notification.models import UserObject,Notifications

# Create your views here.
def seenNotification(request,pk):
    if request.user.is_authenticated:
        user_obj=UserObject.objects.get(user=request.user)
        notificationQs=Notifications.objects.get(id=pk)
        notificationQs.userobj.remove(user_obj)
        notificationQs.is_read=True
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('account:login')