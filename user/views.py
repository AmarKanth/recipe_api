from django.contrib.auth.models import User
from rest_framework import viewsets
from user.serializers import UserSerializer

class UserViewset(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer