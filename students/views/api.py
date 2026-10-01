from ..models.models import Students
from ..serializers.serializers import StudentSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

class StudentsView(APIView):
    
    def get(self, request):
        student = Students.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(
            {
                "message" : "success",
                "status" : True,
                "data" : serializer.data
                
            },
            status=status.HTTP_200_OK
            )
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message" : "Student Created!",
            "status" : True,
            
        }, status=status.HTTP_200_OK)
        

class StudentViewDetails(APIView):
        
        def put(self, request, pk):
            student = Students.objects.get(pk=pk)
            serializer = StudentSerializer(student, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                "message" : "Student Updated!",
                "status" : True
            }, status= status.HTTP_200_OK)

        def delete(self, request, pk):
            student = Students.objects.get(pk=pk)
            student.delete()
            return Response({
                "message" : f"student with id: {pk} is deleted",
                "status" : True
            }, status=status.HTTP_200_OK)
    
    
    
