# from ..models.models import Employers
# from rest_framework import serializers

# class EmployerSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Employers
#         fields = ['id', 'owner', 'company_name', 'is_stable', 'profit', 'office_address']
#         read_only_fields = ['id']
        
from ..models.models import Employers
from bank.models.models import Banks
from employee.models.model import Employee
from rest_framework import serializers

class BanksMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banks
        fields = ['id', 'bank_name', 'bank_code', 'bank_address', 'gross_amount']

class EmployeeMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'salary', 'profession']

class EmployerSerializers(serializers.ModelSerializer):
    banks = BanksMiniSerializer(many=True, read_only=True, source='banks_set')
    employees = EmployeeMiniSerializer(many=True, read_only=True, source='employee_set')

    class Meta:
        model = Employers
        fields = ['id', 'owner', 'company_name', 'is_stable', 'profit', 'office_address', 'banks', 'employees']
        read_only_fields = ['id']