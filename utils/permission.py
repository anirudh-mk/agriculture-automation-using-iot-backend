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


