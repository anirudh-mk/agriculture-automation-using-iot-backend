from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    date_joined = None

    id = models.CharField(primary_key=True, default=uuid.uuid4(), max_length=36)
    username = models.CharField(unique=True, max_length=100)
    profile_pic = models.ImageField(max_length=200, upload_to='user/', null=True, blank=True)
    email = models.CharField(unique=True, max_length=200)
    phone = models.CharField(unique=True, max_length=15, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    @classmethod
    def email_exists(cls, email):
        return cls.objects.filter(email=email).exists()

    class Meta:
        db_table = 'user'


class Farm(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4())
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'farm'


class UserFarmLink(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4())
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='user_farm_link_farm')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_farm_link_user')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_farm_link'


class Vegetable(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4())
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'vegetable'
