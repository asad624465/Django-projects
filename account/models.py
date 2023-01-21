from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver 
#from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

class CustomManager(BaseUserManager):
    def create_user(self,email, username,password,**extra_fields):
        if not email:
            raise ValueError('Email address is required')
        email=self.normalize_email(email)
        user=self.model(email=email,username=username,**extra_fields)
        #user.set_password(make_password(password))
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email, username,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_verify',True)
        extra_fields.setdefault('user_type','developer')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be is_superuser=True')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must be is_active=True')
        if extra_fields.get('is_verify') is not True:
            raise ValueError('Superuser must be is_verify=True')
        
        return  self.create_user(email,username,password,**extra_fields)  

class User(AbstractBaseUser,PermissionsMixin):
    USER_TYPE=(
        ('visitor','visitor'),
        ('developer','developer'),
    )

    email=models.EmailField(unique=True, max_length=50)
    username=models.CharField(unique=True, max_length=100)
    REQUIRED_FIELDS=['username']
    USERNAME_FIELD='email'
    user_type=models.CharField(choices=USER_TYPE, max_length=100,default=USER_TYPE[0])

    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_verify=models.BooleanField(default=False)
    #user_type=models.BooleanField(default=False)

    objects=CustomManager()
    def __str__(self):
        return str(self.email)
    

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    full_name=models.CharField(max_length=100,blank=True,null=True)
    address=models.TextField(max_length=300,blank=True,null=True)
    country=models.CharField(max_length=100,blank=True,null=True)
    city=models.CharField( max_length=100,blank=True,null=True)
    zip_code=models.CharField(max_length=50,blank=True,null=True)
    phone=models.CharField(max_length=16,blank=True,null=True)
    email=models.CharField(max_length=100,blank=True,null=True)
    createdate=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

@receiver(post_save, sender=User)
def create_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_profile(sender,instance, **kwargs):
    instance.profile.save()
    

    

    
