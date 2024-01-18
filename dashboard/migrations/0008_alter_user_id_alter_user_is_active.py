# Generated by Django 5.0.1 on 2024-01-17 10:13

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0007_alter_user_id_alter_user_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.CharField(
                default=uuid.UUID("9efee45b-5df3-4f9d-a0c1-eeb6b4d0e4f7"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(),
        ),
    ]