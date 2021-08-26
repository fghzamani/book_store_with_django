from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer,Address,Staff,User


# admin.site.register(User,UserAdmin)
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")
    search_fields = ("last_name__startswith", )
    fields = ('email','first_name','last_name','password', 'date_joined')
    readonly_fields = [
        'date_joined','last_login'
    ]
    def get_queryset(self, request):
        return User.objects.filter(is_staff=False)
  
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    search_fields = ("last_name__startswith", )
    list_display = ('email','is_staff','is_superuser')
    readonly_fields = ['last_login']
    def get_queryset(self, request):
        return User.objects.filter(is_staff=True)

admin.site.register(Address)