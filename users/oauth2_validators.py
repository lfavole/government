from django.http import HttpRequest
from oauth2_provider.oauth2_validators import OAuth2Validator

class CustomOAuth2Validator(OAuth2Validator):
    def get_additional_claims(self, request: HttpRequest):
        return {
            "given_name": request.user.first_name,
            "family_name": request.user.last_name,
            "name": request.user.get_full_name(),
            "preferred_username": request.user.username,
            "email": request.user.email,
        }
