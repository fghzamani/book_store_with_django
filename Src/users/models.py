from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group

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
class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50, blank=True,null=True)
    last_name = models.CharField(max_length=50,blank=True,null=True)
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,)
    address = models.ForeignKey(Address,on_delete = models.DO_NOTHING,related_name='user',blank=True,null=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):

        """Does the user have a specific permission?"
           Simplest possible answer: Yes, always"""
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin


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
        return self.user.email

