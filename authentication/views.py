from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token


class Logout(APIView):

	def delete(self, request):
		Token.objects.filter(user=request.user).delete()
		return Response(status=status.HTTP_204_NO_CONTENT)