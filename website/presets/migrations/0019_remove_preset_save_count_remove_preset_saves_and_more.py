# Generated by Django 4.1.3 on 2023-01-07 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("presets", "0018_alter_preset_pub_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="preset",
            name="save_count",
        ),
        migrations.RemoveField(
            model_name="preset",
            name="saves",
        ),
        migrations.AlterField(
            model_name="preset",
            name="description",
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name="preset",
            name="name",
            field=models.CharField(max_length=60),
        ),
    ]
