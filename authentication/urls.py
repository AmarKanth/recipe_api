from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView, TokenBlacklistView


urlpatterns = [
    path('token/create/', TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_balcklist'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]