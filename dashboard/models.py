from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    date_joined = None

    id = models.CharField(primary_key=True, default=uuid.uuid4(), max_length=36)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'
