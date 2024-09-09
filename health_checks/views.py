from rest_framework.views import APIView
from rest_framework.response import Response


def get_instance_ip():
	try:
		token_url = "http://169.254.169.254/latest/api/token"
		headers = {"X-aws-ec2-metadata-token-ttl-seconds": "21600"}
		token_response = requests.put(token_url, headers=headers)

		if token_response.status_code == 200:
			token = token_response.text
			metadata_url = "http://169.254.169.254/latest/meta-data/local-ipv4"
			metadata_headers = {"X-aws-ec2-metadata-token": token}
			ip_response = requests.get(metadata_url, headers=metadata_headers)

			if ip_response.status_code == 200:
				return ip_response.text
			else:
				return "Unable to fetch IP"
		else:
			return "Unable to retrieve token"

	except requests.RequestException as e:
		return f"Error: {e}"

class HealthCheck(APIView):
	def get(self, request):
		return Response({"data":"App is up and running"})

class GetIPAdrress(APIView):
	def get(self, request):
		ip_address = get_instance_ip()
		return Response({"instance_ip": ip_address})