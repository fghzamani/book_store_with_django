from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register',views.user_register,name='register'),
    path('login',views.user_login,name='login'),
    path('dashboard/',views.user_dasshboard,name='dashboard'),
    path('dashboard/addreses/',views.add_new_address,name = 'user addresses'),
    path('logout/',views.user_logout,name='logout'),

    # urls for change password
    path('password_reset/',auth_views.PasswordResetView.as_view(),name = 'password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),


]