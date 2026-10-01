# from django.urls import path
# from ..views.api import ProductView, ProductViewEdit

# urlpatterns = [
#     path('new_products/', ProductView.as_view(), name='ProductView'),
#     path('new_products/<int:pk>/', ProductViewEdit.as_view(), name='ProductViewEdit')
# ]

from rest_framework.routers import DefaultRouter
from ..views.api import ProductView

router = DefaultRouter()
router.register('new_products', ProductView, basename='ProductView')

urlpatterns = router.urls
