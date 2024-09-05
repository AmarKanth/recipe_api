from rest_framework.views import APIView
from rest_framework.response import Response


class HealthCheck(APIView):
	def get(self, request):
		return Response({"data":"App is up and running"})

class GetIPAdrress(APIView):
	def get(self, request):
		return Response({'ip': request.META.get('REMOTE_ADDR')})