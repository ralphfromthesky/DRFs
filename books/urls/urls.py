from django.urls import path
from ..views.api import BooksView, BooksViewEdit

urlpatterns = [
    path('new_books/', BooksView.as_view(), name='BooksView'),
    path('new_books/<int:pk>/', BooksViewEdit.as_view(), name='BooksViewEdit')

]