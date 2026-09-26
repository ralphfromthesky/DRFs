from django.urls import path, include
from ..views.api import EmployeeView

urlpatterns = [
    path('newEmployee/', EmployeeView.as_view(), name='EmployeeView')
]