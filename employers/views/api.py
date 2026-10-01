from  ..models.models import Employers
from ..serializers.serializers import EmployerSerializers
from config.pagination.pagination import GlobalPagination
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

class EmployerViews(APIView):
    
    def post(self, request):
        serializer = EmployerSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message" : "Successfully Saved!",
            "status" : True,
        }, status=status.HTTP_201_CREATED)


    def get(self, request):
        # employer = Employers.objects.all()  
        # serializer = EmployerSerializers(employer, many=True)
        # return Response({
        #     "status" : True,
        #     "data" : serializer.data,
        # }, status=status.HTTP_200_OK)
        employer = Employers.objects.all().order_by('id')
        paginator = GlobalPagination()
        page = paginator.paginate_queryset(employer, request, view=self)
        serializer = EmployerSerializers(page, many=True)
        return paginator.get_paginated_response(serializer.data)
        
        
class EmployerViewEdit(APIView):
    
    def delete(self, request, pk):
        employer = Employers.objects.get(pk=pk)
        employer.delete()
        return Response({
            "message" : f"employer with the id {pk} is deleted!",
            "status" : True,
        }, status=status.HTTP_200_OK)
        
    def put(self, request, pk):
        employer = Employers.objects.get(pk=pk)
        serializer = EmployerSerializers(employer, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message" : f"Employer with the id {pk} is editted!",
            "status" : True,
        }, status=status.HTTP_200_OK)

