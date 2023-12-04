# Generated by Django 4.1.3 on 2022-12-02 10:04

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("presets", "0003_alter_preset_image_file_alter_preset_json_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="preset",
            name="like",
            field=models.ManyToManyField(
                related_name="preset_liked_by_users", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="preset",
            name="save",
            field=models.ManyToManyField(
                related_name="preset_saved_by_users", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="preset",
            name="image_file",
            field=models.ImageField(upload_to="images"),
        ),
        migrations.AlterField(
            model_name="preset",
            name="pub_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 12, 2, 5, 4, 28, 636055),
                verbose_name="date published",
            ),
        ),
    ]
