from rest_framework import serializers

class StatusStatisticsSerializer(serializers.Serializer):
    interventionstatus = serializers.CharField()
    total = serializers.IntegerField()
