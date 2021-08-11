from django.contrib import admin
from .models import Book,Category,Coupon
# Register your models here.


admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Coupon)