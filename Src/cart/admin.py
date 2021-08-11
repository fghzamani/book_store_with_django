from django.contrib import admin
from .models import Order,Orderdetail,Discount,Cart



admin.site.register(Order)
admin.site.register(Orderdetail)
admin.site.register(Discount)
admin.site.register(Cart)