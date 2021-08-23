from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer,Address,Staff,User

# Register your models here.

admin.site.register(User,UserAdmin)
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields = ('username',)

    def get_queryset(self, request):
        return User.objects.filter(is_staff=False)

# admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Staff)