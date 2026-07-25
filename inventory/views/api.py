from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status



from django.http import HttpResponse

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def showResponse(request):
    return Response({
        "message" : True,
        "token" : True
    }, status=status.HTTP_200_OK)
# def showResponse(request):
#     return HttpResponse('hello ralph')