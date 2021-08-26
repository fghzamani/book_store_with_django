from django.contrib import admin
from .models import Discount

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_filter = ('active', )
    list_display=['code','amount','active']