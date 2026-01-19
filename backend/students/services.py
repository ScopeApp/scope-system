# backend/students/services.py
from django.db.models import Count
from students.models import Students


def get_students_count_by_class():
    stats = Students.objects.values('classid__classname').annotate(
        total_students=Count('studentid')
    ).order_by('classid__classname')

    return stats