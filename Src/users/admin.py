from django.contrib import admin
from .models import Customer,Address,Staff
from django.contrib.auth.models import User
# Register your models here.


# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     fields = ('username',)

#     def get_queryset(self, request):
#         return User.objects.filter(is_staff=False)






admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Staff)