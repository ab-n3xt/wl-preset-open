# Generated by Django 4.1.3 on 2023-01-07 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("presets", "0019_remove_preset_save_count_remove_preset_saves_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="preset",
            name="description",
            field=models.CharField(max_length=600),
        ),
    ]
