from ..models.model import Employee
from ..serializers.serializers import EmployeeSerializer
from rest_framework.permissions import AllowAny

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class EmployeeView(APIView):
    permission_classes = [AllowAny] # ito per function kung allowed kahit hnid nakalogin

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message" : "Employee Created",
                "status"  : True
            }, status=status.HTTP_201_CREATED
        )
        
    def get(self, request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)
    
class EmployeDetailView(APIView):
        permission_classes = [AllowAny] # ito per function kung allowed kahit hnid nakalogin
        
        def put(self, request, pk):
            employee = Employee.objects.get(pk=pk)
            serializer = EmployeeSerializer(employee, data=request.data)    
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {
                "message" : "Employee Updated",
                "status" : True
            }, status=status.HTTP_200_OK
            )
            
        def delete(self, request, pk):
            employee = Employee.objects.get(pk=pk)
            employee.delete()
            return Response(
                {
                    "message" : f"Employee deleted = {pk}",
                    "status" : True
                },
                status=status.HTTP_200_OK
            )
            
            