from ..models.models import Police
from ..seriliazers.serializers import PoliceSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class PoliceViews(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = PoliceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message":"Succesfully saved!",
            "status" : True
        }, status=status.HTTP_200_OK)        
        