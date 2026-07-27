from django.urls import path, include
from ..views.api import ItemView, ItemDetailView

urlpatterns = [
    path('item/', ItemView.as_view()),
    path('item/<int:pk>/', ItemDetailView.as_view()),
]