# Generated by Django 4.1.3 on 2023-01-29 01:04

from django.db import migrations, models
import presets.validators.validators


class Migration(migrations.Migration):

    dependencies = [
        ('presets', '0033_alter_preset_zip_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preset',
            name='thumbnail_file',
            field=models.ImageField(default='images/default.jpg', upload_to='images', validators=[presets.validators.validators.valid_image_size]),
        ),
        migrations.AlterField(
            model_name='preset',
            name='zip_file',
            field=models.FileField(default='zip_files/default.zip', upload_to='zip_files', validators=[presets.validators.validators.valid_preset_size, presets.validators.validators.valid_zip]),
        ),
    ]