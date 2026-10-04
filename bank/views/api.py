from  ..models.models import Banks
from ..serializers.serializers import BankSerializers

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from rest_framework.viewsets import ModelViewSet

class BankModelViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = BankSerializers
    queryset = Banks.objects.all().order_by('id')
    

# class BankViews(APIView):
#     permission_classes = [AllowAny]
    
#     def post(self, request):
#         serializer = BankSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#             "message": "Bank save successfully!",
#             "status" : True,
#         }, status=status.HTTP_201_CREATED)
        
#     def get(self, request):
#         bank = Banks.objects.all()
#         serializer = BankSerializers(bank, many=True)
#         return Response({
#             "status" : True,
#             "data" : serializer.data
#         }, status=status.HTTP_200_OK)
        
        
# class BankViewsEdit(APIView):
    permission_classes = [AllowAny]
    
    def delete(self, request, pk):
        bank = Banks.objects.get(pk=pk)
        bank.delete()
        return Response({
            "message" : f"Bank with the id {pk} is deleted!",
            "status" : True,
        }, status=status.HTTP_200_OK)
        
    def put(self, request, pk):
        bank = Banks.objects.get(pk=pk)
        serializer = BankSerializers(bank, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message" : f"Bank with id {pk} id editted!",
            "status" : True,
        }, status=status.HTTP_200_OK)