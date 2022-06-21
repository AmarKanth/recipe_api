from django.urls import path
from authentication.views import Logout
from rest_framework.authtoken.views import ObtainAuthToken


urlpatterns = [
    path('token/', ObtainAuthToken.as_view()),
    path('logout/', Logout.as_view()),
]