from django.urls import path
from ..views.api import PoliceViews

urlpatterns = [
    path('new_police/', PoliceViews.as_view(), name='PoliceViews')
]