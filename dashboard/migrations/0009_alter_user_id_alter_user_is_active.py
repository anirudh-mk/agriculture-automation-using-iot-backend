# Generated by Django 5.0.1 on 2024-01-17 10:14

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0008_alter_user_id_alter_user_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.CharField(
                default=uuid.UUID("1f711207-e886-478e-828a-e53a548fbaed"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]