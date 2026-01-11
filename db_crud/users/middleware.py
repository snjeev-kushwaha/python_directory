from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import User

def jwt_authenticate(request):
    auth = JWTAuthentication()

    header = auth.get_header(request)
    if header is None:
        raise AuthenticationFailed('Authorization header missing')

    raw_token = auth.get_raw_token(header)
    if raw_token is None:
        raise AuthenticationFailed('Invalid token')

    validated_token = auth.get_validated_token(raw_token)

    user_id = validated_token.get('user_id')
    if not user_id:
        raise AuthenticationFailed('Invalid token payload')

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise AuthenticationFailed('User not found')

    return user
