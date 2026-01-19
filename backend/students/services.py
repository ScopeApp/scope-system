

from django.db.models import Count
from .models import Students

def get_student_status_statistics():
    """
    פונקציה ששולפת את כל הסטטוסים ומחזירה ספירה של כל אחד.
    תוצאה לדוגמה: [{' interventionstatus': 'active', 'total': 10}, {'status': 'inactive', 'total': 2}]
    """
    return Students.objects.values('interventionstatus').annotate(total=Count('interventionstatus'))