from django.db import models
from users.models import Customer , Address
from products.models import Book
from discount.models import Discount



class Order(models.Model):
   
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE , related_name='invoices')
    state = models.BooleanField(default = False) # shows the state of order(false for not paid and true for paid and finished orders)
    created_date = models.DateTimeField(auto_now_add=True)
    billing_address = models.ForeignKey(Address,on_delete=models.CASCADE,related_name='add')
    total_price = models.BigIntegerField()
    discount = models.ForeignKey(Discount,on_delete= models.DO_NOTHING,blank = True,null=True)
     
    class Meta:
        ordering = ('-created_date',)
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'
   
    def __str__(self):
        return f'Order {self.id}'

  



class Orderdetail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    book = models.ForeignKey(Book, on_delete =models.DO_NOTHING)
    unit_price = models.IntegerField()
    quantity =models.IntegerField(default=1)
    class Meta:
        verbose_name = 'جزئیات سفارش'
        verbose_name_plural = 'جزئیات سفارش ها'

    def __str__(self):
        return str(self.id)
        
    def get_cost(self):
        return self.unit_price * self.quantity


