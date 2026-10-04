# from django.urls import path
# from ..views.api import BankViews, BankViewsEdit

# urlpatterns = [
#     path('new_bank/', BankViews.as_view(), name='BankViews'),
#     path('new_bank/<int:pk>/', BankViewsEdit.as_view(), name='BankViewsEdit')
# ]

from rest_framework.routers import DefaultRouter
from ..views.api import BankModelViewSet

router = DefaultRouter()
router.register('new_bank', BankModelViewSet, basename='BankModelViewSet')
urlpatterns = router.urls