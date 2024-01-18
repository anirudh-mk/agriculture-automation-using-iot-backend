# Generated by Django 5.0.1 on 2024-01-17 19:28

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0012_alter_farm_id_alter_user_id_alter_farm_table"),
    ]

    operations = [
        migrations.AddField(
            model_name="farm",
            name="description",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="farm",
            name="id",
            field=models.CharField(
                default=uuid.UUID("b3a1a1f9-a8c7-4deb-8468-fd74477206fb"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.CharField(
                default=uuid.UUID("f8980e97-2ee5-44d2-a68b-d3b448817c43"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
