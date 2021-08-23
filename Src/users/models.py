from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser ,BaseUserManager
from django.contrib.auth.models import Group
from django.contrib.auth.models import UserManager


# class UserManager(BaseUserManager):
#     def create_user(self,first_name,last_name, email,address, password=None, is_admin=False, is_staff=False, is_active=True):
#         if not email:
#             raise ValueError("User must have an email")
#         if not password:
#             raise ValueError("User must have a password")
#         if not address:
#              raise ValueError("User must have an address")

#         user = self.model(
#             email=self.normalize_email(email)
#         )
    
#         user.set_password(password)  # change password to hash
#         user.address = address
#         user.admin = is_admin
#         user.staff = is_staff
#         user.active = is_active
#         user.save(using=self._db)
#         return user
        
#     def create_superuser(self, email, password=None):
#         if not email:
#             raise ValueError("User must have an email")
#         if not password:
#             raise ValueError("User must have a password")
        

#         user = self.model(
#             email=self.normalize_email(email)
#         )
       
#         user.set_password(password)
#         user.admin = True
#         user.staff = False
#         user.active = True
#         user.save(using=self._db)
#         return user

class Address(models.Model):
    """
   model for managing addresses of customers

    """
    CITY_CHOICE = [
        ('Al','البرز'),
        ('Te','تهران'),
        ('Az_E','آذربایجان شرقی'),
        ('Az_W','آذربایجان غربی'),
        ('Ko_N','خراسان شمالی'),
        ('Ko_S','خراسان جنوبی'),
        ('Ko_C','خراسان مرکزی'),
        ('Si','سیستان و بلوچستان'),
        ('Mar','مرکزی'),
        ('Go','گلستان'),
        ('Gi','گیلان'),
        ('Ha','همدان'),
        ('Lo','لرستان'),
        ('Ku','خوزستان'),
        ('Kerman','کرمان'),
        ('Ker','کرمانشاه'),
        ('Char','چهارمحال و بختیاری'),
        ('Es','اصفهان'),
        ('Eil','ایلام'),
        ('Bu','بوشهر'),
        ('Zan','زنجان'),
        ('Sem','سمنان'),
        ('Fars','فارس'),
        ('Ghaz','قزوین'),
        ('Ghom','قم'),
        ('Koh','کهگیلویه و بویراحمد'),
        ('Maz','مازندران'),
        ('Hor','هرمزگان'),
        ('Yaz','یزد'),

    ]
    city = models.CharField(max_length=7,choices = CITY_CHOICE)
    Address = models.TextField(max_length=1000)
    postal_code = models.CharField(max_length=20)
    is_default = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'نشانی'
        verbose_name_plural = 'نشانی ها'
class User(AbstractUser):
    
    
    address = models.ForeignKey(Address,on_delete = models.DO_NOTHING,related_name='user',blank=True,null=True)
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

