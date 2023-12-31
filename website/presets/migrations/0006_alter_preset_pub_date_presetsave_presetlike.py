# Generated by Django 4.1.3 on 2022-12-03 07:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('presets', '0005_remove_preset_like_remove_preset_save_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preset',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 3, 2, 25, 43, 839226), verbose_name='date published'),
        ),
        migrations.CreateModel(
            name='PresetSave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='presets.preset')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PresetLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='presets.preset')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
