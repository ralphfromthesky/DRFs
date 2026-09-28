from ..models.models import Students
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id', 'full_name', 'address', 'course', 'isStudy']
        read_only_fields = ['id']