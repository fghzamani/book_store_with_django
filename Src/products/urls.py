from django.urls import path
from .views import  BookDetailForm_func,HomeView,CategoryListView,BookDetailView,SearchList,BookDetailForm_ ,CategoryDetailView 
from . import views



urlpatterns = [
path('', HomeView.as_view(), name='index'),
path('books/all-books/', views.products, name='book_list'),
path('books/detail/<int:pk>', BookDetailView.as_view(),name='book_detail'),
# path('books/detail/<int:pk>', BookDetailForm_func_view,name='book_detail'),
path('category/<slug:category_slug>',views.products,name='category_detail'),
path('all-categories/',CategoryListView.as_view(),name='all_categories'),
path('search/', SearchList.as_view(), name='search'),
]
