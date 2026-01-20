from django.urls import path
from . import views
from .views import StudentDistributionView

urlpatterns = [
    path('distribution/', StudentDistributionView.as_view(), name='student-distribution'),
    path('stats/', views.StudentStatusStatsView.as_view(), name='student-stats'),
    path('all-detailed/', views.StudentReportView.as_view(), name='student-all-detailed')

]