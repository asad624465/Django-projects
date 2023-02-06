from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User=get_user_model()

class UserObject(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    createdate=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.user.email} notifications objects"
    @receiver(post_save, sender=User)
    def create_notification_object(sender,instance,created, **kwargs):
        if created:
            UserObject.objects.create(user=instance)
        instance.userobject.save()
        
    
    
    
class Notifications(models.Model):
    userobj=models.ManyToManyField(UserObject, blank=True) 
    message=models.TextField()
    is_read=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.message)
    

