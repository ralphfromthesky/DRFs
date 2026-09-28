from django.urls import path
from ..views.api import GamersView, GamersViewEdit

urlpatterns = [
    path('new_gamers/', GamersView.as_view(), name='GamersView'),
    path('new_gamers/<int:pk>/', GamersViewEdit.as_view(), name='GamersViewEdit')

]