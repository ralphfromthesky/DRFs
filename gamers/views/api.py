from ..models.models import Gamers
from ..serializers.serializers import GamerSerializers

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

class GamersView(APIView):
    
    def post(self, request):
        serializer = GamerSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "messsage" : "Succesfully Saved!",
            "status" : True
        }, status=status.HTTP_201_CREATED)
        
    def get(self, request):
        gamers = Gamers.objects.all()
        serializers = GamerSerializers(gamers, many=True)
        return Response({
            "status" : True,
            "data" : serializers.data
        }, status=status.HTTP_200_OK)
        
class GamersViewEdit(APIView):
    
    def delete(self, request, pk):
        gamer = Gamers.objects.get(pk=pk)
        gamer.delete()
        return Response({
            "message" : f"Gamer withe the id of {pk} is deleted!"
        }, status=status.HTTP_200_OK)
        
    def put(self, request, pk):
        gamer = Gamers.objects.get(pk=pk)
        serializer = GamerSerializers(gamer, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message" : f"Gamer with the id of {pk} is editted!",
            "status" : True
        }, status=status.HTTP_200_OK)