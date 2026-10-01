# from django.urls import path
# from ..views.api import ItemViews, ItemEditViews

# urlpatterns = [
#     path('new_items/', ItemViews.as_view(), name='ItemViews'),
#     path('new_items/<int:pk>/', ItemEditViews.as_view(), name='ItemEditViews')
# ]

from rest_framework.routers import DefaultRouter
from ..views.api import ItemViews


router = DefaultRouter()
router.register('new_items', ItemViews, basename='ItemViews')

urlpatterns = router.urls