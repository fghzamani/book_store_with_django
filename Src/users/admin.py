from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer,Address,Staff,User

class AddressInline(admin.TabularInline):
    model = Address
    raw_id_fields =('customer',)
    search_fields =('customer',)
# admin.site.register(User,UserAdmin)
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name",'email','date_joined')
    search_fields = ("last_name", )
    fields = ('email','first_name','last_name','password', 'date_joined')
    inlines =(AddressInline,)
    readonly_fields = ['date_joined','last_login']
    
    def get_queryset(self, request):
        return User.objects.filter(is_staff=False)
  
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    search_fields = ("last_name","first_name" )
    list_display = ('email','is_staff','is_superuser','date_joined')
    readonly_fields = ['last_login','date_joined']

    def get_queryset(self, request):
        return User.objects.filter(is_staff=True)

# admin.site.register(Address)
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    search_fields = ("city",)
    list_display = ('city','address','postal_code','customer')
    list_filter =('city',)
   
    