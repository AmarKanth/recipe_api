from django.urls import path, include
from health_checks.views import HealthCheck

urlpatterns = [
	path('health-checks/', HealthCheck.as_view()),
]