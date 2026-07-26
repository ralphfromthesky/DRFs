from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.models import Item
from ..serializers.serializers import ItemSerializer
from accounts.permissions.permissions import RoleBasedPermission

class ItemView(APIView):
    permission_classes = [RoleBasedPermission]
    
    # GET — lahat pwede (viewer, editor, admin)
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    
    # POST — viewer, editor, admin pwede
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "Item created successfully."},
            status=status.HTTP_201_CREATED
        )
    
    # PUT — editor, admin pwede
    def put(self, request, pk):
        item = Item.objects.get(pk=pk)
        serializer = ItemSerializer(item, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "Item updated successfully."},
            status=status.HTTP_200_OK
        )
    
    # DELETE — admin lang pwede
    def delete(self, request, pk):
        item = Item.objects.get(pk=pk)
        item.delete()
        return Response(
            {"message": "Item deleted successfully."},
            status=status.HTTP_200_OK
        )