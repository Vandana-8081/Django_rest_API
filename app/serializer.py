from .models import Employee
from rest_framework import serializers

class EmployeeSerializer(serializers.Serializer):
    name =serializers.CharField(max_length=30)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20)
    phone = serializers.CharField(max_length=10)


    def create(self , validated_data):
       print("create method called...")
       return  Employee.objects.create(**validated_data)
    
    def update(self , employee , validated_data):
        newEmployee = Employee(**validated_data)
        newEmployee.id = employee.id
        newEmployee.save()
        return newEmployee


class UserSerializer(serializers.Serializer):
    username =serializers.CharField(max_length=30)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20)
    first_name =serializers.CharField(max_length=30)
    
