from django.urls import path
from . import views  # ייבוא יחסי של הפונקציות (views) מתוך אותה תיקייה
from students.views import StudentDistributionView

urlpatterns = [
    # # נתיב לבדיקת הסטטוס של השרת/המודלים (למשל: /students/status/)
    # path('status/', views.check_status, name='students_status_check'),
    #
    # # נתיב לקבלת כל הסטודנטים (למשל: /students/all/)
    # path('all/', views.get_all_students, name='get_all_students'),
    path('distribution/', StudentDistributionView.as_view(), name='student-distribution'),
    path('stats/', views.StudentStatusStatsView.as_view(), name='student-stats'),


]