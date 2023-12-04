# Generated by Django 4.1.3 on 2023-01-11 19:31

from django.db import migrations, models
import presets.validators.validators


class Migration(migrations.Migration):

    dependencies = [
        ("presets", "0024_preset_user_who_submitted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="preset",
            name="thumbnail_file",
            field=models.ImageField(
                upload_to="images",
                validators=[presets.validators.validators.valid_image_size],
            ),
        ),
    ]
