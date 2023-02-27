from rest_framework import serializers
from .models import Department, Employee

class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('depId', 'depName')
        
class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('empId', 'empName', 'depName', 'joiningDate', 'photoName')