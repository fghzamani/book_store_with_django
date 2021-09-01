from django.contrib import admin
from .models import Order,Orderdetail

class OrderDetailInline(admin.TabularInline):
    model = Orderdetail
    raw_id_fields =('order',)
    search_fields =('order')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines =(OrderDetailInline,)
    list_filter = ("customer","state",'created_date' )
    search_fields = ("customer", )
    list_display=["customer","state",'total_price']
   


# admin.site.register(Orderdetail)
@admin.register(Orderdetail)
class OrderdetailAdmin(admin.ModelAdmin):
    list_display=['order','book','quantity','unit_price']
    
    list_filter =('book',)