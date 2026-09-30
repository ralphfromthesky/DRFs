from django.urls import path
from ..views.api import ProductView, ProductViewEdit

urlpatterns = [
    path('new_products/', ProductView.as_view(), name='ProductView'),
    path('new_products/<int:pk>/', ProductViewEdit.as_view(), name='ProductViewEdit')
]