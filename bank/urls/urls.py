from django.urls import path
from ..views.api import BankViews, BankViewsEdit

urlpatterns = [
    path('new_bank/', BankViews.as_view(), name='BankViews'),
    path('new_bank/<int:pk>/', BankViewsEdit.as_view(), name='BankViewsEdit')
]