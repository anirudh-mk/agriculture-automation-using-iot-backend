# Generated by Django 5.0.1 on 2024-01-26 13:16

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "dashboard",
            "0019_alter_farm_id_alter_user_id_alter_user_profile_pic_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="farm",
            name="id",
            field=models.CharField(
                default=uuid.UUID("dd85c41f-5a65-423a-bbf0-338df86a3305"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.CharField(
                default=uuid.UUID("e70cc9fe-eafb-424a-867f-ec27c168b2fe"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="userfarmlink",
            name="id",
            field=models.CharField(
                default=uuid.UUID("46ced817-99ee-4477-8fa2-16d03aa53373"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="vegetable",
            name="id",
            field=models.CharField(
                default=uuid.UUID("09c059b7-3123-4b78-9763-f06f29b03d2e"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]