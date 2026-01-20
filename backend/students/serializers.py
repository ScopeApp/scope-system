# backend/students/serializers.py
from rest_framework import serializers
from .models import Students

class ClassDistributionSerializer(serializers.Serializer):
    className = serializers.CharField(source='classid__classname')
    studentCount = serializers.IntegerField(source='total_students')
from rest_framework import serializers


class StatusStatisticsSerializer(serializers.Serializer):
    interventionstatus = serializers.CharField()
    total = serializers.IntegerField()


class StudentReportSerializer(serializers.ModelSerializer):

    class_name = serializers.CharField(source='classid.classname', read_only=True)

    class Meta:
        model = Students
        fields = [
            'studentid',
            'firstname',
            'lastname',
            'class_name',
            'interventionstatus',
            'studenttz'
        ]