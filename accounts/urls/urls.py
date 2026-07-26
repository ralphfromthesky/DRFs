from django.urls import path
from ..views.api import RegisterView, LoginView, AssignRoleView, UserListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('assignRole/', AssignRoleView.as_view(), name='assign'),
    path('registerList/', UserListView.as_view(), name='list')
]