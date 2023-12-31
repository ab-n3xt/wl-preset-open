# Generated by Django 4.1.3 on 2022-12-31 23:56

import datetime
from django.db import migrations, models
import presets.validators.validators


class Migration(migrations.Migration):

    dependencies = [
        ("presets", "0013_alter_preset_pub_date_alter_preset_zip_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="preset",
            name="pub_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 12, 31, 18, 56, 26, 810966),
                verbose_name="date published",
            ),
        ),
        migrations.AlterField(
            model_name="preset",
            name="zip_file",
            field=models.FileField(
                upload_to="zip_files",
                validators=[
                    presets.validators.validators.valid_preset_size,
                    presets.validators.validators.valid_zip,
                ],
                null=True,
                blank=True
            ),
        ),
    ]
