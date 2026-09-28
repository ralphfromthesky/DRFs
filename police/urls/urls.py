from django.urls import path
from ..views.api import PoliceViews, PoliceViewEdiDelete

urlpatterns = [
    path('new_police/', PoliceViews.as_view(), name='PoliceViews'),
    path('new_police/<int:pk>/', PoliceViewEdiDelete.as_view(), name='PoliceViewEdiDelete')
    
]