from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    is_superuser = None
    is_staff = None

    qr_code = models.CharField(
        unique=True,
        max_length=36,
        default=uuid.uuid4()
    )
