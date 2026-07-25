from django.urls import path
from ..views.api import RegisterView, LoginView, AssignRoleView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('assignRole/', AssignRoleView.as_view(), name='assign')
]