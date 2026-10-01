from ..models.models import Police
from ..seriliazers.serializers import PoliceSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class PoliceViews(APIView):
    
    def post(self, request):
        serializer = PoliceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message":"Succesfully saved!",
            "status" : True
        }, status=status.HTTP_200_OK)
        
        
    def get(self, request):
        police = Police.objects.all()
        serializer = PoliceSerializer(police, many=True)        
        return Response({
            "status" : True,
            "data" : serializer.data
        }, status=status.HTTP_200_OK)
        
class PoliceViewEdiDelete(APIView):
    
    def delete(self, request, pk):
        police = Police.objects.get(pk=pk)
        police.delete()
        return Response({
            "message" : f"the police withe the id of {pk} is deleted",
           "status" : True 
        }, status=status.HTTP_200_OK)
        
    def put(self, request, pk):
        police = Police.objects.get(pk=pk)
        serialize = PoliceSerializer(police, data= request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response({
            "message" : f"the police with the id of {pk} is editted!",
            "status" : True
        }, status=status.HTTP_200_OK) 