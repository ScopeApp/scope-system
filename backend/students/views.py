# from django.shortcuts import render
# from django.http import HttpResponse
# from django.http import JsonResponse
#
# def check_status(request):
#     # מחזירה תגובת טקסט פשוטה לבדיקה
#     return HttpResponse("Backend is running and models are ready!")
#
# def get_all_students(request):
#
#     from .models import Students
#     try:
#         # קריאת כל האובייקטים של Students (מקביל ל-SELECT * FROM Students)
#         students_data = Students.objects.all()
#
#         # בניית רשימת נתונים (Dicts) להמרה ל-JSON
#         data = []
#         for student in students_data:
#             data.append({
#                 'id': student.studentid,
#                 'tz': student.studenttz,
#                 'first_name': student.firstname,
#                 'last_name': student.lastname,
#                 # כדי לגשת לשם הכיתה או ה-ID של הכיתה, אנחנו משתמשים בשם המודל הקשור (Classes).
#                 # מאחר שמודל Classes קיים, הגישה דרך .classid עובדת.
#                 'class_id': student.classid.classid,
#                 'intervention_status': student.interventionstatus,
#             })
#
#         # JsonResponse ממיר את רשימת ה-Dicts ל-JSON
#         return JsonResponse(data, safe=False)
#
#     except Exception as e:
#         # אם יש שגיאה (כמו שגיאת DB), נחזיר הודעת שגיאה ברורה
#         return JsonResponse({'error': str(e)}, status=500)


# backend/students/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from students.services import get_students_count_by_class
from .serializers import ClassDistributionSerializer
from drf_spectacular.utils import extend_schema


class StudentDistributionView(APIView):
    @extend_schema(responses=ClassDistributionSerializer(many=True))
    def get(self, request):
        # 1. שליפת הנתונים מהשירות
        data = get_students_count_by_class()

        # 2. המרה ל-JSON (many=True כי זו רשימה של אובייקטים)
        serializer = ClassDistributionSerializer(data, many=True)

        # 3. שליחת תשובה מסודרת
        return Response(serializer.data, status=status.HTTP_200_OK)
