# Generated by Django 4.1.3 on 2023-01-10 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("presets", "0020_alter_preset_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="preset",
            name="name",
            field=models.CharField(max_length=30),
        ),
    ]
