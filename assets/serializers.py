from rest_framework import serializers
from .models import Asset, Assignment, MaintenanceLog

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

class AssignmentSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'


class MaintenanceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model= MaintenanceLog
        fields = '__all__'