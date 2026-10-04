from ..models.models import Items
from ..serializers.serilalizers import ItemsSerializers

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from rest_framework.exceptions import PermissionDenied # kung nakalogin

from rest_framework import filters  #para sa filter
from django_filters.rest_framework import DjangoFilterBackend #para sa filter


# class ItemViews(APIView):
#     permission_classes = [AllowAny]
    
#     def post(self, request):
#         serializer = ItemsSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#             "message": "Item saved!",
#             "status" : True,
#         }, status=status.HTTP_201_CREATED)
        
        
#     def get(self, request):
#         items = Items.objects.all()
#         serializer = ItemsSerializers(items, many=True)
#         return Response(
#             {
#             "status" : True,
#             "ako si" : "ralph",
#             "data" : serializer.data
#         }, status=status.HTTP_200_OK)
        
        
class ItemViews(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Items.objects.all().order_by('id')
    serializer_class = ItemsSerializers
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter] #para sa filter
    filterset_fields = ['is_available'] #para sa filter
    search_fields = ['item_name', 'item_descriptions'] #para sa filter search bar
    ordering_fields = ['value', 'item_count'] #para sa filter at ordering ng number

    def get_queryset(self):  #for fetching his own items
        if self.request.user.is_authenticated:
            return Items.objects.filter(owner=self.request.user)
        return Items.objects.none()
        
    def perform_create(self, serializer): #for saving own numbers
        if self.request.user.is_authenticated:
            serializer.save(owner=self.request.user)
        else:
            raise PermissionDenied("Login Please!")
            
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            "message": "Item Saved",
            "status": True,
            "data": response.data
        }, status=status.HTTP_201_CREATED)
            
#class ItemEditViews(APIView):
        # permission_classes = [AllowAny]
            
        # def delete(self, request, pk):
        #     item = Items.objects.get(pk=pk)
        #     item.delete()
        #     return Response({
        #         "message" : f"Item with the id {pk} is deleted!",
        #         "status" : True,
        #     }, status=status.HTTP_200_OK)
            
        # def put(self, request, pk):
        #     item = Items.objects.get(pk=pk)
        #     serializer = ItemsSerializers(item, data=request.data)
        #     serializer.is_valid(raise_exception=True)
        #     serializer.save()
        #     return Response({
        #         "message" : f"Item with the id {pk} is editted!",
        #         "status" : True,
        #     }, status=status.HTTP_200_OK)