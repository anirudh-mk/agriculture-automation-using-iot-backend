# Generated by Django 5.0.1 on 2024-01-17 19:10

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0011_farm_alter_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="farm",
            name="id",
            field=models.CharField(
                default=uuid.UUID("0170d8e7-ffd3-4417-bb5c-f4901d2c0406"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.CharField(
                default=uuid.UUID("1ac9aa70-2df3-492f-83af-8157127036a0"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterModelTable(
            name="farm",
            table="farm",
        ),
    ]
