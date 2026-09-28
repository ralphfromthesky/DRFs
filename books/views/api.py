from ..models.models import Book
from ..serialzers.serializers import BookSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


class BooksView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message" : 'Successfull saved!',
            "status" : True
        }, status=status.HTTP_200_OK)
        
        
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({
            "status" : 200,
            "data" : serializer.data
        }, status=status.HTTP_200_OK)
        