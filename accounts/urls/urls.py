from django.urls import path
from ..views.api import LogoutView, RegisterView, LoginView, AssignRoleView, UserListView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('assignRole/', AssignRoleView.as_view(), name='assign'),
    path('registerList/', UserListView.as_view(), name='list'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]