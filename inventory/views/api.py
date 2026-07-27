from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.models import Item
from ..serializers.serializers import ItemSerializers
from accounts.permissions.permissions import RoleBasedPermission


class ItemView(APIView):
    permission_classes = [RoleBasedPermission]
    
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializers(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ItemSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "Item created successfully."},
            status=status.HTTP_201_CREATED
        )


class ItemDetailView(APIView):
    permission_classes = [RoleBasedPermission]
    
    def put(self, request, pk):
        item = Item.objects.get(pk=pk)
        serializer = ItemSerializers(item, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "Item updated successfully."},
            status=status.HTTP_200_OK
        )
    
    def delete(self, request, pk):
        item = Item.objects.get(pk=pk)
        item.delete()
        return Response(
            {
                "message": f"Item deleted successfully - with key {pk}."

             },
            status=status.HTTP_200_OK
        )