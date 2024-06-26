# Generated by Django 5.0.1 on 2024-04-21 02:19

import django.contrib.auth.models
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Farm",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.UUID("c67c8484-2d4e-4f0e-a6e1-dcb08fc32f45"),
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("description", models.CharField(max_length=1000, null=True)),
                ("location", models.CharField(max_length=200)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "farm",
            },
        ),
        migrations.CreateModel(
            name="Vegetable",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.UUID("0f57b380-560c-42b7-baeb-f07e85a8dfe2"),
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("n", models.CharField(max_length=20)),
                ("p", models.CharField(max_length=20)),
                ("k", models.CharField(max_length=20)),
                ("time_required", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "vegetable",
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "id",
                    models.CharField(
                        default=uuid.UUID("30edcf5b-8ede-4025-be82-2edb2de0bc9b"),
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                ("username", models.CharField(max_length=100, unique=True)),
                (
                    "profile_pic",
                    models.ImageField(
                        blank=True, max_length=200, null=True, upload_to="user/"
                    ),
                ),
                ("email", models.CharField(max_length=200, unique=True)),
                ("phone", models.CharField(max_length=15, unique=True)),
                ("password", models.CharField(max_length=200)),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "db_table": "user",
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="UserFarmLink",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.UUID("5f674c00-61a6-4c76-b787-0729af1122d2"),
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("is_completed", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "farm",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_farm_link_farm",
                        to="dashboard.farm",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_farm_link_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "user_farm_link",
            },
        ),
        migrations.CreateModel(
            name="FarmVegetableLink",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.UUID("9359986e-a042-4537-858e-a71d210cc827"),
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("is_completed", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "farm",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="farm_vegetable_link_farm",
                        to="dashboard.farm",
                    ),
                ),
                (
                    "vegetable",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="farm_vegetable_link_vegetable",
                        to="dashboard.vegetable",
                    ),
                ),
            ],
            options={
                "db_table": "farm_vegetable_link",
            },
        ),
    ]
