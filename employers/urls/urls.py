from django.urls import path
from ..views.api import EmployerViews, EmployerViewEdit

urlpatterns = [
    path('new_employers/', EmployerViews.as_view(), name='EmployerViews'),
    path('new_employers/<int:pk>/', EmployerViewEdit.as_view(), name='EmployerViewEdit')
]