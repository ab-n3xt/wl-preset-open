# Generated by Django 4.1.3 on 2023-01-13 21:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("presets", "0029_alter_preset_created_at_alter_preset_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="preset",
            name="created_at",
            field=models.DateTimeField(
                db_index=True, default=django.utils.timezone.now
            ),
        ),
        migrations.AlterField(
            model_name="preset",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
