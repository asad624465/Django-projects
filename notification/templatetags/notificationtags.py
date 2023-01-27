from django import template
from notification.models import UserObject,Notifications
register=template.Library()

@register.filter
def Notification(user):
    if user.is_authenticated:
        user_obj=UserObject.objects.get(user=user)
        notification=Notifications.objects.filter(userobj=user_obj,is_read=False).order_by('-id')
        if notification.exists():
            return notification
        else:
            return None
    else:
        return None
@register.filter
def CountNotification(user):
    if user.is_authenticated:
        user_obj=UserObject.objects.get(user=user)
        notification=Notifications.objects.filter(userobj=user_obj,is_read=False)
        if notification.exists():
            return notification.count()
        else:
            return 0
    else:
        return 0