# Generated by Django 5.0.1 on 2024-01-29 16:06

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0032_alter_farm_id_alter_farmvegetablelink_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="farm",
            name="id",
            field=models.CharField(
                default=uuid.UUID("5df91674-cc4e-4e65-b991-a63d171b2294"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="farmvegetablelink",
            name="id",
            field=models.CharField(
                default=uuid.UUID("09eb98d0-826b-4497-80b0-2e4a31db372d"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.CharField(
                default=uuid.UUID("a43b2ac5-3225-446c-a2e7-50d7afab3d94"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="userfarmlink",
            name="id",
            field=models.CharField(
                default=uuid.UUID("80c6d482-ed52-454f-8ca1-96b558a5e74e"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="vegetable",
            name="id",
            field=models.CharField(
                default=uuid.UUID("859ee999-8608-4010-9894-6bf5fbd22c26"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]