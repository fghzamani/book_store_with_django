from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
from users.models import Customer
from products.models import Book 
from users.models import Address

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete = models.DO_NOTHING , related_name='invoices')
    order_date = models.DateTimeField(auto_now_add=True)
    billing_address = models.ForeignKey(Address,on_delete=models.CASCADE,related_name='address')
    total_price = models.BigIntegerField()

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'

class Orderdetail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    book = models.ForeignKey(Book, on_delete =models.DO_NOTHING)
    unit_price = models.IntegerField()
    quantity =models.IntegerField(default=1)



class Discount(models.Model):
    code = models.CharField(max_length=250)
    amount = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(1)])
    created_date = models.TimeField(auto_now_add=True)
    expired_date = models.DateTimeField()
    class Meta:
        verbose_name = 'تخفیف'
        verbose_name_plural = 'تخفیف ها'

class Cart(models.Model):
    STATE_CHOISE= [('O','ordered'),('u','unconfirmed')]
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    state = models.CharField(max_length=1,choices = STATE_CHOISE,default='u')
    discount = models.ForeignKey(Discount,on_delete=models.CASCADE,blank=True,null=True)
    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبدهای خرید'



