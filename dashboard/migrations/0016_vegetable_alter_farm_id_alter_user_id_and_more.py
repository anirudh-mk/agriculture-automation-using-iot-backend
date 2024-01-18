# Generated by Django 5.0.1 on 2024-01-18 09:09

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0015_rename_farm_id_userfarmlink_farm_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Vegetable",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.UUID("5f6aa350-c358-475e-88b9-8ff8adbb30df"),
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "vegetable",
            },
        ),
        migrations.AlterField(
            model_name="farm",
            name="id",
            field=models.CharField(
                default=uuid.UUID("548fa42b-d0b4-461a-b080-e22c619c5931"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.CharField(
                default=uuid.UUID("cd3da646-cf12-4ba1-a245-e9d0b0400d1a"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="userfarmlink",
            name="id",
            field=models.CharField(
                default=uuid.UUID("4c14d50f-ece4-402d-8da0-84c24211792b"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
