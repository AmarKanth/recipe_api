from django.contrib.auth.models import AnonymousUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

class SkipPublicUrls(TokenAuthentication):

	def authenticate(self, request):
		skip_urls = ['/api/token/', '/api/docs/', '/api/schema/']

		if request.path in skip_urls:
			return (AnonymousUser, None)

		auth = request.META.get('HTTP_AUTHORIZATION', b'').split()

		if len(auth) <= 1:
			raise AuthenticationFailed('Invalid token header. No credentials provided.')

		if auth[0].lower() != self.keyword.lower():
			raise AuthenticationFailed('Invalid Keyword.')

		return self.authenticate_credentials(auth[1])