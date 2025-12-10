from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def check_status(request):
    # מחזירה תגובת טקסט פשוטה לבדיקה
    return HttpResponse("Backend is running and models are ready!")

def get_all_students(request):
    """
    קורא את כל הסטודנטים מטבלת ה-DB ומחזיר JSON.
    """
    from .models import Students
    try:
        # קריאת כל האובייקטים של Students (מקביל ל-SELECT * FROM Students)
        students_data = Students.objects.all()

        # בניית רשימת נתונים (Dicts) להמרה ל-JSON
        data = []
        for student in students_data:
            data.append({
                'id': student.studentid,
                'tz': student.studenttz,
                'first_name': student.firstname,
                'last_name': student.lastname,
                # כדי לגשת לשם הכיתה או ה-ID של הכיתה, אנחנו משתמשים בשם המודל הקשור (Classes).
                # מאחר שמודל Classes קיים, הגישה דרך .classid עובדת.
                'class_id': student.classid.classid,
                'intervention_status': student.interventionstatus,
            })

        # JsonResponse ממיר את רשימת ה-Dicts ל-JSON
        return JsonResponse(data, safe=False)

    except Exception as e:
        # אם יש שגיאה (כמו שגיאת DB), נחזיר הודעת שגיאה ברורה
        return JsonResponse({'error': str(e)}, status=500)
