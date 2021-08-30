from django.urls import path
from . import views


urlpatterns = [
  path('create/', views.order_create,name='order_create'),
  path('order/process/',views.process_order,name = 'order_process'),
  path('created/',views.created_order,name = 'order_created'),
  
]