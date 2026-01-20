# backend/students/services.py
from django.db.models import Count
from .models import Students


def get_students_count_by_class():
    stats = Students.objects.values('classid__classname').annotate(
        total_students=Count('studentid')
    ).order_by('classid__classname')
    return stats

def get_student_status_statistics():
    return Students.objects.values('interventionstatus').annotate(total=Count('interventionstatus'))


def get_all_students_report():
    return Students.objects.select_related('classid').all()

