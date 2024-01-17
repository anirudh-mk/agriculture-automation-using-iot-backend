from datetime import datetime, timedelta

import decouple
import jwt
from rest_framework import authentication
from rest_framework.permissions import BasePermission
from rest_framework.serializers import ValidationError

from dashboard.models import User


class CustomException(ValidationError):
    def __init__(self, detail='Something went wrong', status_code=403):
        self.detail = detail
        self.status_code = status_code


class CustomizePermission(BasePermission):
    def authenticate(self, request):
        try:
            token = authentication.get_authorization_header(request).decode("utf-8").split()
            if token[0] != "Bearer" and len(token) != 2:
                exception_message = {"hasError": True, "message": "Invalid token", "statusCode": 1000}
                raise CustomException(exception_message)
            return self._authenticate_credentials(request, token[1])
        except Exception:
            exception_message = {"hasError": True, "message": "Invalid token", "statusCode": 1000}
            raise CustomException(exception_message)

    def _authenticate_credentials(self, request, token):
        payload = jwt.decode(token, 'SEDKLK23D@LK323#@!2', algorithms=["HS256"], verify=True)

        id = payload.get("id", None)
        expiry = payload.get("expiry", None)
        if id and expiry:
            # if expiry check expiry and return Token Expired
            user = User.objects.filter(id=id)
            if user.exists():
                return user.first(), payload
            else:
                pass
        return None, payload


class JWTUtils:

    @staticmethod
    def fetch_user_id(request):
        token = authentication.get_authorization_header(request).decode("utf-8").split()
        payload = jwt.decode(token[1], 'SEDKLK23D@LK323#@!2', algorithms=["HS256"], verify=True)
        user_id = payload.get("id")
        if user_id is None:
            raise Exception("The corresponding JWT token does not contain the 'user_id' key")
        return user_id


class TokenGenerate:
    def generate(self, user):
        if user is not None:
            access_expiry_time = datetime.now() + timedelta(seconds=1800)  # 30 minutes
            access_expiry = access_expiry_time.strftime("%d/%m/%Y %H:%M:%S")

            access_token = jwt.encode(
                {'id': user.id, 'expiry': access_expiry,
                 'tokenType': 'access'},
                'SEDKLK23D@LK323#@!2',
                algorithm="HS256")

            refresh_expiry_time = datetime.now() + timedelta(seconds=259200)  # 3 days
            refresh_expiry = refresh_expiry_time.strftime("%d/%m/%Y %H:%M:%S")
            refresh_token = jwt.encode(
                {'id': user.id, 'expiry': refresh_expiry, 'tokenType': 'refresh'},
                'SEDKLK23D@LK323#@!2',
                algorithm="HS256")
            auth = {'accessToken': access_token, 'refreshToken': refresh_token, 'expiry': access_expiry}
        else:
            auth = None
        return auth