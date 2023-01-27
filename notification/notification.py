from notification.models import UserObject,Notifications

class SentNotification:
    def __init__(self, user,message)->None:
        self.user=user
        self.message=message

        user_obj=UserObject.objects.get(user=self.user)
        notification=Notifications.objects.create(message=self.message,is_read=False)
        notification.userobj.add(user_obj)
        notification.save()