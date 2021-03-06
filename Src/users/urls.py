from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register',views.user_register,name='register'),
    path('login',views.user_login,name='login'),
    path('dashboard/',views.user_dasshboard,name='dashboard'),
    path('personal/info/',views.user_update_info,name='change info'),
    path('dashboard/addreses/',views.add_new_address,name = 'user addresses'),
    path('remove/<int:address_id>/', views.remove_address, name='address_remove'),
    path('default/address/', views.change_default_address, name='default_add'),
    path('dashboard/orders/history/',views.user_order_history,name='order history'),
    path('logout/',views.user_logout,name='logout'),

    # urls for change password
    path('password_reset/',auth_views.PasswordResetView.as_view(),name = 'password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),


]