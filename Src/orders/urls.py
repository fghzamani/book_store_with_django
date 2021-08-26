from django.urls import path
from . import views


urlpatterns = [
   path('create/', views.order_create,name='order_create'),
  path('created/',views.created_order,name = 'order_created'),
  # path('admin/order/<int:order_id>/', views.admin_order_detail,name='admin_order_detail'),
]