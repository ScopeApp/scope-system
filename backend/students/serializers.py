# backend/students/serializers.py
from rest_framework import serializers

class ClassDistributionSerializer(serializers.Serializer):
    className = serializers.CharField(source='classid__classname')
    studentCount = serializers.IntegerField(source='total_students')
from rest_framework import serializers

class StatusStatisticsSerializer(serializers.Serializer):
    interventionstatus = serializers.CharField()
    total = serializers.IntegerField()
