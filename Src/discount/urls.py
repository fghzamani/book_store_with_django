from django.urls import path
from . import views

app_name = 'discount'

urlpatterns = [
    path('apply/', views.discount_apply, name='apply'),
]
