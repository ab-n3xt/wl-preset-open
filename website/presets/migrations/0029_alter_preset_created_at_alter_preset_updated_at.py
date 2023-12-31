# Generated by Django 4.1.3 on 2023-01-13 21:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("presets", "0028_preset_view_count"),
    ]

    operations = [
        migrations.AlterField(
            model_name="preset",
            name="created_at",
            field=models.DateField(db_index=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="preset",
            name="updated_at",
            field=models.DateField(auto_now=True),
        ),
    ]
