from django.urls import path
from ..views.api import BooksView

urlpatterns = [
    path('new_books/', BooksView.as_view(), name='BooksView')
]