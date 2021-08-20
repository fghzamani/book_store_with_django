from django.urls import path
from .views import BookListView,HomeView,CategoryListView,BookDetailView,SearchList,BookDetailForm
 

urlpatterns = [
path('', HomeView.as_view(), name='index'),
path('books/all-books/', BookListView.as_view(), name='book_list'),
# path('categories/<slug>/', BookListView.as_view(), name='categories'),
path('books/detail/<int:pk>', BookDetailView.as_view(),name='book_detail'),
path('books/detail/<int:pk>', BookDetailForm.as_view(),name='book_detail'),
path('category/<slug:category_slug>',BookListView.as_view(),name='category_detail'),
path('all-categories/',CategoryListView.as_view(),name='all_categories'),
path('search/', SearchList.as_view(), name='search'),
]
