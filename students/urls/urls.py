from django.urls import path
from ..views.api import StudentsView, StudentViewDetails


urlpatterns = [
    path('newstudents/', StudentsView.as_view(), name='StudentsView'),
    path('newstudents/<int:pk>/', StudentViewDetails.as_view()),
]