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
        
        
        
class BooksViewEdit(APIView):
    permission_classes = [AllowAny]
    
    def delete(self, request, pk):
        books = Book.objects.get(pk=pk)
        books.delete()
        return Response({
            "message" : f"the book with the id {pk} is deleted!"
        }, status=status.HTTP_200_OK)
        
    def put(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "messsage" : f"the book with the id of {pk} is editted!",
            "status" : True
        }, status=status.HTTP_200_OK)
        
