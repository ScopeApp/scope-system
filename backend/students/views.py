from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import get_student_status_statistics
from .serializers import StatusStatisticsSerializer



class StudentStatusStatsView(APIView):
    def get(self, request):
        # קריאה ל-Service
        stats_data = get_student_status_statistics()

        # המרה ל-JSON באמצעות הסריאליזר
        serializer = StatusStatisticsSerializer(stats_data, many=True)

        # החזרת התשובה
        return Response(serializer.data, status=status.HTTP_200_OK)
