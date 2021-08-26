from django.contrib import admin
from .models import Order,Orderdetail

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_filter = ("customer","state" )
    search_fields = ("customer__startswith", )
    list_display=["customer","state",'total_price' ]



admin.site.register(Orderdetail)
