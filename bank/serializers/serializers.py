from ..models.models import Banks
from rest_framework import serializers

class BankSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banks
        fields = ['id', 'bank_name', 'employer', 'bank_code', 'bank_address', 'is_active', 'gross_amount']
        read_only_fields = ['id']
        
        