
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('backend.core_users.urls')),
    path('api/data/', include('backend.students.urls')),
    path('api/interventions/', include('backend.interventions.urls')),
]
