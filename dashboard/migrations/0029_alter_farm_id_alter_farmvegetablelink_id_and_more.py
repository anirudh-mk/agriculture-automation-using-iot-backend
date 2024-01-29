# Generated by Django 5.0.1 on 2024-01-29 16:03

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0028_alter_farm_id_alter_farmvegetablelink_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="farm",
            name="id",
            field=models.CharField(
                default=uuid.UUID("7182f2fc-5029-4137-aa78-912fd5591562"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="farmvegetablelink",
            name="id",
            field=models.CharField(
                default=uuid.UUID("aa74ffb1-0ea8-4e8e-b859-3f299c19faf7"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.CharField(
                default=uuid.UUID("27f9ec1d-33f4-4437-a619-d6450bbdf2ad"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name="userfarmlink",
            name="id",
            field=models.CharField(
                default=uuid.UUID("a3a1c3a7-c0f5-4242-9245-ff7b42adb998"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="vegetable",
            name="id",
            field=models.CharField(
                default=uuid.UUID("781398e6-be93-43a0-9298-f374ea3e2599"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]