from django.urls import path
from . import views



urlpatterns = [
    path('',views.StaffProfileView.as_view(),name='staff_profile'),
    path('new/', views.BookCreateView.as_view(), name='book_new'),
    path('booksall/', views.BookListView.as_view(), name='store_books_list'),
    path('edit/<int:pk>/',views.BookUpdateView.as_view(), name='book_edit'),
    path('delete/<int:pk>/',views.BookDeleteView.as_view(), name='book_delete'),
    path('new/category/', views.NewCategoryView.as_view(), name='category_new'),
    path('new/coupon/', views.NewCouponView.as_view(), name='new_coupon'),
    path('allcoupons/', views.CouponListView.as_view(), name='all_coupon'),
    path('adminreports/', views.StoreReportAdmin.as_view(), name='admin report'),
    path('addnewstaff/',views.NewStaffCreateView.as_view(),name = 'add staff'),
]