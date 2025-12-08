# backend/interventions/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # נתיב להוספת דיווח תקופתי (מורה/רכז)
    path('report/add/', views.add_progress_update, name='add_update'),
    # נתיב לעדכון הסטטוס הכולל (מורה/רכז)
    path('status/update/', views.update_student_status, name='update_status'),
]