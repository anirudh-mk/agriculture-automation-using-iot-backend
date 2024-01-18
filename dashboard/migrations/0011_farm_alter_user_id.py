# Generated by Django 5.0.1 on 2024-01-17 19:09

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0010_alter_user_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Farm",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.UUID("ed55ec80-c92f-4ce2-afa4-d2155e97aa8f"),
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.CharField(
                default=uuid.UUID("b50eef75-f149-4278-9809-0688b46665fa"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
