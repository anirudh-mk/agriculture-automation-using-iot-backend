from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    date_joined = None

    id = models.CharField(primary_key=True, default=uuid.uuid4(), max_length=36)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(unique=True, max_length=100)
    profile_pic = models.ImageField(max_length=200, upload_to='user/', null=True, blank=True)
    email = models.CharField(unique=True, max_length=200)
    phone = models.CharField(unique=True, max_length=15)
    password = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    @classmethod
    def email_exists(cls, email):
        return cls.objects.filter(email=email).exists()

    class Meta:
        db_table = 'user'


class Vegetable(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4())
    name = models.CharField(max_length=200, null=False, blank=False)
    n = models.CharField(max_length=20)
    p = models.CharField(max_length=20)
    k = models.CharField(max_length=20)
    time_required = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'vegetable'


class Farm(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4())
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, null=True)
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'farm'


class UserFarmLink(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4())
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='user_farm_link_farm')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_farm_link_user')
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_farm_link'


class FarmVegetableLink(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4())
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='farm_vegetable_link_farm')
    vegetable = models.ForeignKey(Vegetable, on_delete=models.CASCADE, related_name='farm_vegetable_link_vegetable')
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'farm_vegetable_link'


class FarmNPKLink(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4())
    n = models.CharField(max_length=20)
    p = models.CharField(max_length=20)
    k = models.CharField(max_length=20)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='farm_npk_link_farm')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'farm_npk_link'