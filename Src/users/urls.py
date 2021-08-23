from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register',views.user_register,name='register'),
    path('login',views.user_login,name='login'),
    # path('dashboard',index,name='dashboard'),
    path('logout/',views.user_logout,name='logout'),
]