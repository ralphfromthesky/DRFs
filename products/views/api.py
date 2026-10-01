# from  ..models.models import Product
# from ..serializers.serializers import ProductSerializers
# from config.pagination.pagination import GlobalPagination

# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny
# from rest_framework.views import APIView
# from rest_framework import status

# class ProductView(APIView):
#     permission_classes = [AllowAny]
    
#     def post(self, request):
#         serializer = ProductSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#             "message" : "Successfully saved!",
#             "statu" : True,
#         }, status=status.HTTP_201_CREATED)
        
        
#     def get(self, request):
#         # product = Product.objects.all()
#         # serializer = ProductSerializers(product, many=True)
#         # return Response({
#         #     "status" : True,
#         #     "data" : serializer.data,
#         # }, status=status.HTTP_200_OK) 
#         product = Product.objects.all().order_by('id')
#         paginator = GlobalPagination()
#         paginator.page_size = 20 # wtite mo ito kung ang mismong app need ng mas malaki ang page_size kc ang global is 5 lang ata

#         page = paginator.paginate_queryset(product, request, view=self)
#         serializer = ProductSerializers(page, many=True)
#         return paginator.get_paginated_response(serializer.data)
        
        
# class ProductViewEdit(APIView):
#     permission_classes = [AllowAny]
    
#     def delete(self, request, pk):
#         product = Product.objects.get(pk=pk)
#         product.delete()
#         return Response({
#             "message" : f"Product with the id {pk} is deleted!",
#             "status" : True,
#         }, status=status.HTTP_200_OK)
        
#     def put(self, request, pk):
#         product = Product.objects.get(pk=pk)
#         serializer = ProductSerializers(product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#             "message" : f"Product with the id {pk} is editted!",
#             "status" : True
#         }, status=status.HTTP_200_OK)
    
    
from ..models.models import Product
from ..serializers.serializers import ProductSerializers

from rest_framework import viewsets
from rest_framework.permissions import AllowAny


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializers
