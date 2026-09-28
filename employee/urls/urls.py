from django.urls import path, include
from ..views.api import EmployeeView, EmployeDetailView

urlpatterns = [
    path('newEmployee/', EmployeeView.as_view(), name='EmployeeView'),
    path('newEmployee/<int:pk>/', EmployeDetailView.as_view()),
]