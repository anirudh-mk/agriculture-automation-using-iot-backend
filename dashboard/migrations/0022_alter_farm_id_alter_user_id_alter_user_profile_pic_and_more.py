# Generated by Django 5.0.1 on 2024-01-26 13:20

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "dashboard",
            "0021_alter_farm_id_alter_user_id_alter_userfarmlink_id_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="farm",
            name="id",
            field=models.CharField(
                default=uuid.UUID("9c696e50-2411-4e81-abf4-d7b713fa2109"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.CharField(
                default=uuid.UUID("50d5b639-1bd6-4ec9-b8bd-f861dbd58df8"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="profile_pic",
            field=models.ImageField(
                blank=True, max_length=200, null=True, upload_to="user/"
            ),
        ),
        migrations.AlterField(
            model_name="userfarmlink",
            name="id",
            field=models.CharField(
                default=uuid.UUID("0ee01d12-ae37-48aa-b4cc-36cd562b56cb"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="vegetable",
            name="id",
            field=models.CharField(
                default=uuid.UUID("3230c345-1ba2-4417-92b7-c42f11e6f160"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
