# Generated by Django 4.1.3 on 2023-01-03 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("presets", "0017_alter_preset_character_alter_preset_pub_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="preset",
            name="pub_date",
            field=models.DateTimeField(auto_now=True, verbose_name="date published"),
        ),
    ]
