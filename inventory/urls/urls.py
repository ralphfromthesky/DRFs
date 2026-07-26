from django.urls import path, include
from ..views.api import ItemView

urlpatterns = [
    path('item/', ItemView.as_view()),
    path('item/<int:pk>/', ItemView.as_view()),

]