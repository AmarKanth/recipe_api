from django.utils.deprecation import MiddlewareMixin

from rest_framework import exceptions
from rest_framework.authtoken.models import Token


class TokenAuthentication(MiddlewareMixin):

	def process_request(self, request):
		skip_urls = ['/api/token/', '/api/docs/', '/api/schema/']

		if request.path not in skip_urls:
			auth = request.META.get('HTTP_AUTHORIZATION', b'').split()

			if len(auth) <= 1:
				msg = 'Please provide token for auth verification.'
				raise exceptions.AuthenticationFailed(msg)

			try:
				user = Token.objects.get(key=auth[1]).user
			except Token.DoesNotExist:
				msg = 'Invalid token.'
				raise exceptions.AuthenticationFailed(msg)

			request.user = user