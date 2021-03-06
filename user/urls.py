from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user import views


router = DefaultRouter()
router.register('', views.UserViewset)

urlpatterns = [
	path('user/', include(router.urls)),
]