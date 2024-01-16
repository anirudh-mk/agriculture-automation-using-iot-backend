# Generated by Django 5.0.1 on 2024-01-16 09:22

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="qr_code",
            field=models.CharField(
                default=uuid.UUID("1433616e-7ae4-47df-8ed7-702f7e2a2c46"),
                max_length=36,
                unique=True,
            ),
        ),
    ]
