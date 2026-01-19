from django.urls import path
from . import views  # ייבוא יחסי של הפונקציות (views) מתוך אותה תיקייה

urlpatterns = [
    path('stats/', views.StudentStatusStatsView.as_view(), name='student-stats'),

]