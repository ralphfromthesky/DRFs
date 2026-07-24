from django.urls import path, include
from ..views.api import showResponse 


urlpatterns = [
    path('item/', showResponse, name='inventory')
]