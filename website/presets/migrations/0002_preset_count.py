# Generated by Django 4.1.3 on 2022-11-28 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("presets", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="preset",
            name="count",
            field=models.IntegerField(default=0),
        ),
    ]
