
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('backend.core_users.urls')),
    path('api/data/', include('backend.students.urls')),
    path('api/interventions/', include('backend.interventions.urls')),

     path('api/data/students/', include('backend.students.urls')),
# נתיבי Swagger המקצועיים

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # הכתובת הזו תפתח לך את ממשק ה-Swagger בדפדפן
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
