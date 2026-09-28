from ..models.models import Police
from rest_framework import serializers

class PoliceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Police
        fields = ['id', 'name', 'rank', 'salary', 'isWorking']
        read_only_fields = ['id']
        