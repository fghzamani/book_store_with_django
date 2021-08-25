from django.contrib import admin
from .models import Book,Category,Coupon
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ("category", )


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_filter =("coupon_type",)


admin.site.register(Category)