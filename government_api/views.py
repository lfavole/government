from allauth.account.models import EmailAddress
from django.http import HttpRequest, JsonResponse
from django.contrib.auth.decorators import login_required

from users.models import User

@login_required
def userinfo(request: HttpRequest):
    if not hasattr(request, "access_token"):
        return JsonResponse({"error": "invalid_request"}, status=400)
    user: User = request.user
    ret = {
        "sub": str(user.id),
        "scopes": request.access_token.scopes,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "username": user.username,
        "emails": [
            {
                "email": email.email,
                "primary": email.primary,
                "verified": email.verified,
            }
            for email in EmailAddress.objects.filter(user=user)
        ],
    }
    return JsonResponse(ret)
