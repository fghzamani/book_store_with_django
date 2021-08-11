from django.contrib import admin
from .models import Customer,Staff,Address
# Register your models here.


admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Staff)