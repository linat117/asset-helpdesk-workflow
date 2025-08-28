from rest_framework import serializers
from .models import Employee, Department 
from accounts.models import User
from django.contrib.auth.hashers import make_password
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True, required=False)
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = Employee
        fields = ['id','first_name','last_name','email','department','role','username','password','confirm_password']
    
    def validate(self, data):
        # Check if passwords match when creating user account
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            raise serializers.ValidationError("Passwords don't match")
        
        return data
    def create(self, validated_data):
        # Extract user creation data
        username = validated_data.pop('username', None)
        password = validated_data.pop('password', None)
        confirm_password = validated_data.pop('confirm_password', None)
        
        # Create employee
        employee = Employee.objects.create(**validated_data)
        
        # Create user account if credentials provided
        if username and password:
            try:
                user = User.objects.create(
                    username=username,
                    email=employee.email,
                    password=make_password(password),
                    role=employee.role,
                    first_name=employee.first_name,
                    last_name=employee.last_name
                )
                # Link employee to user
                employee.user = user
                employee.save()
            except Exception as e:
                employee.delete()
                raise serializers.ValidationError(f"Failed to create user account: {str(e)}")
        
        return employee