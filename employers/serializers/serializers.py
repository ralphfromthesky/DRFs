from ..models.models import Employers
import re

from rest_framework import serializers

class EmployerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employers
        fields = ['id', 'owner', 'company_name', 'is_stable', 'profit', 'office_address']
        read_only_fields = ['id']
        
    
    
    def validate_owner(self, value):
        if re.search(r'\d', value):
            raise serializers.ValidationError('no number pls')
        return value
