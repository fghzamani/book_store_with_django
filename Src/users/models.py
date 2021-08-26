from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser ,BaseUserManager
from django.contrib.auth.models import Group
from django.contrib.auth.models import UserManager



class User(AbstractUser):
    
    # username = None
    
    email = models.EmailField(unique =True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.


    def __str__(self):
        return self.email




class Customer(User):
    """
    model for customer of bookstore

    """
    
    class Meta:
        proxy = True
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتری ها'
    def __str__(self):
        return self.email
    

class Staff(User):
    class Meta:
        proxy=True
        verbose_name ='کارمند'
        verbose_name_plural = 'کارمندان'
    def __str__(self):
        return self.email


class Address(models.Model):
    """
   model for managing addresses of customers

    """
    CITY_CHOICE = [
        ('البرز','البرز'),
        ('تهران','تهران'),
        ('آذربایجان شرقی','آذربایجان شرقی'),
        ('آذربایجان غربی','آذربایجان غربی'),
        ('خراسان شمالی','خراسان شمالی'),
        ('خراسان جنوبی','خراسان جنوبی'),
        ('خراسان مرکزی','خراسان رضوی'),
        ('سیستان و بلوچستان','سیستان و بلوچستان'),
        ('مرکزی','مرکزی'),
        ('گلستان','گلستان'),
        ('گیلان','گیلان'),
        ('همدان','همدان'),
        ('لرستان','لرستان'),
        ('خوزستان','خوزستان'),
        ('کرمان','کرمان'),
        ('کرمانشاه','کرمانشاه'),
        ('چهارمحال و بختیاری','چهارمحال وبختیاری'),
        ('اصفهان','اصفهان'),
        ('ایلام','ایلام'),
        ('بوشهر','بوشهر'),
        ('زنجان','زنجان'),
        ('سمنان','سمنان'),
        ('فارس','فارس'),
        ('قزوین','قزوین'),
        ('قم','قم'),
        ('کهگیلویه و بویراحمد','کهگیلویه و بویراحمد'),
        ('مازندران','مازندران'),
        ('هرمزگان','هرمزگان'),
        ('یزد','یزد'),

    ]
    city = models.CharField(max_length=50,choices = CITY_CHOICE)
    address = models.TextField(max_length=1000)
    postal_code = models.CharField(max_length=20)
    is_default = models.BooleanField(default=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'نشانی'
        verbose_name_plural = 'نشانی ها'