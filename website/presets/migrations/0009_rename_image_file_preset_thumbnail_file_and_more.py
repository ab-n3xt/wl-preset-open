# Generated by Django 4.1.3 on 2022-12-23 06:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("presets", "0008_remove_presetsave_preset_remove_presetsave_user_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="preset",
            old_name="image_file",
            new_name="thumbnail_file",
        ),
        migrations.RemoveField(
            model_name="preset",
            name="json_file",
        ),
        migrations.AddField(
            model_name="preset",
            name="zip_file",
            field=models.FileField(default=None, upload_to="zip_files", null=True, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="preset",
            name="pub_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 12, 23, 1, 35, 28, 739551),
                verbose_name="date published",
            ),
        ),
    ]