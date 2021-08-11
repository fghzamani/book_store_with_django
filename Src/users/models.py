from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group


class Address(models.Model):
    """
   model for managing addresses of customers

    """
    Address = models.TextField(max_length=1000)


class Customer(models.Model):
    """
    model for customer of bookstore

    """
    user= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.ManyToManyField(Address,related_name='user')
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True)
    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتری ها'
    def __str__(self):
        return self.user.username
    

class Staff(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email=models.EmailField(verbose_name='email address',max_length=255,unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=70)
    class Meta:
        verbose_name ='کارمند'
        verbose_name_plural = 'کارمندان'
    def __str__(self):
        return self.user.username
