from django.urls import path, include
from health_checks.views import HealthCheck, GetIPAdrress

urlpatterns = [
	path('health-checks/', HealthCheck.as_view()),
	path('ip/', GetIPAdrress.as_view())
]