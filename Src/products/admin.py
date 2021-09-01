from django.contrib import admin
from .models import Book,Category,Coupon
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ("category",'author', )
    search_fields = ("author",'title' )
    list_display = ('title','coupon','inventory','number_of_sell','price')
    list_display_links = ('title',)
    # def categories(self,obj):
    #     return [cat.title for cat in obj.category.all()]


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_filter =("coupon_type",'is_active')
    list_display = ('created_date','expired_date','cash_amount','percent_amount','is_active')
   

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields ={'slug':('name',)}
    search_fields =('name',)


